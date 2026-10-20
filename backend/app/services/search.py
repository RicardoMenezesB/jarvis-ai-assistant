from __future__ import annotations

import os
from typing import Any

import httpx

from app.config import settings


class LLMService:
    async def generate(self, prompt: str, context: str = "") -> str:
        if settings.groq_api_key:
            return await self._generate_with_groq(prompt, context)
        return self._fallback_response(prompt, context)

    async def _generate_with_groq(self, prompt: str, context: str) -> str:
        headers = {
            "Authorization": f"Bearer {settings.groq_api_key}",
            "Content-Type": "application/json",
        }
        body = {
            "model": settings.groq_model,
            "messages": [
                {"role": "system", "content": "Você é PC, um assistente premium de voz e IA. Responda de maneira direta, proativa e útil."},
                {"role": "user", "content": f"Contexto da memória:\n{context}\n\nPergunta:\n{prompt}"},
            ],
            "temperature": 0.7,
        }

        try:
            async with httpx.AsyncClient(timeout=30.0) as client:
                response = await client.post(
                    "https://api.groq.com/openai/v1/chat/completions",
                    headers=headers,
                    json=body,
                )
                response.raise_for_status()
                payload = response.json()
                return payload["choices"][0]["message"]["content"].strip()
        except Exception:
            return self._fallback_response(prompt, context)

    def _fallback_response(self, prompt: str, context: str) -> str:
        lower = prompt.lower()

        if "pesquise" in lower or "web" in lower or "internet" in lower:
            return (
                "Vou buscar o tema no contexto disponível e te devolver um resumo objetivo. "
                "Se você configurar uma API de busca, PC pode pesquisar em tempo real e citar fontes."
            )

        if "código" in lower or "python" in lower or "programa" in lower or "react" in lower:
            return (
                "Posso ajudar a estruturar o código, organizar a arquitetura e sugerir implementações. "
                "Se quiser, posso criar uma base para API, app web, automação ou script funcional."
            )

        if "roteiro" in lower or "vídeo" in lower or "script" in lower:
            return (
                "Claro. Vou transformar a ideia em roteiro, estrutura de cenas, tom de voz e objetivos claros para produção."
            )

        if "lembre" in lower or "memória" in lower:
            return "Entendido. Vou armazenar esse contexto e usá-lo nas próximas interações para personalizar melhor a experiência."

        return (
            "PC ativo. Posso ajudar com pesquisa, programação, planejamento, roteiros e automação. "
            f"No momento, o contexto relevante é: {context[:220]}"
        )

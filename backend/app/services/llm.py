from __future__ import annotations

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
                {
                    "role": "system",
                    "content": (
                        "Você é PC, um assistente premium de IA de voz e produtividade. "
                        "Responda com clareza, personalidade premium, contexto e ação prática."
                    ),
                },
                {
                    "role": "user",
                    "content": f"Contexto:\n{context}\n\nPergunta:\n{prompt}",
                },
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
        text = prompt.lower()

        if any(keyword in text for keyword in ["pesquise", "procure", "buscar", "internet", "web", "notícia", "noticias"]):
            return (
                "PC está preparado para pesquisar e resumir as fontes mais relevantes. "
                "Se você configurar uma API de busca, posso trazer citações e análise em tempo real."
            )

        if any(keyword in text for keyword in ["código", "codigo", "programar", "python", "react", "app", "api", "backend", "frontend"]):
            return (
                "Posso estruturar o projeto, escrever a arquitetura, criar os arquivos e te entregar um MVP pronto para evoluir."
            )

        if any(keyword in text for keyword in ["roteiro", "vídeo", "video", "script", "conteúdo", "conteudo"]):
            return (
                "Claro. Vou transformar a sua ideia em roteiro, sequência narrativa, objetivos e estrutura de produção com tom profissional."
            )

        if any(keyword in text for keyword in ["lembre", "memória", "perfil", "aprender", "preferência", "preferencia"]):
            return "Entendido. Vou registrar esse contexto e usá-lo nas próximas interações para personalizar melhor a experiência."

        return (
            "PC online e pronto. Posso pesquisar, criar código, organizar tarefas, escrever roteiros e ajudar com decisões. "
            f"Contexto atual: {context[:220]}"
        )

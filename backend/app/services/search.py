from __future__ import annotations

from typing import Any

import httpx

from app.config import settings


class LLMService:
    async def generate(self, prompt: str, context: str = "") -> str:
        if settings.provider == "groq" and settings.groq_api_key:
            return await self._generate_groq(prompt, context)
        if settings.provider == "openrouter" and settings.openrouter_api_key:
            return await self._generate_openrouter(prompt, context)
        if settings.provider == "openai" and settings.openai_api_key:
            return await self._generate_openai(prompt, context)
        if settings.provider == "ollama":
            return await self._generate_ollama(prompt, context)
        return self._fallback_response(prompt, context)

    async def _generate_groq(self, prompt: str, context: str) -> str:
        headers = {"Authorization": f"Bearer {settings.groq_api_key}", "Content-Type": "application/json"}
        payload = {
            "model": settings.groq_model,
            "messages": [
                {"role": "system", "content": "Você é PC, um assistente premium de IA de voz e produtividade. Responda com clareza, personalidade premium e ação prática."},
                {"role": "user", "content": f"Contexto:\n{context}\n\nPergunta:\n{prompt}"},
            ],
            "temperature": 0.7,
        }
        try:
            async with httpx.AsyncClient(timeout=30) as client:
                response = await client.post("https://api.groq.com/openai/v1/chat/completions", headers=headers, json=payload)
                response.raise_for_status()
                data = response.json()
                return data["choices"][0]["message"]["content"].strip()
        except Exception:
            return self._fallback_response(prompt, context)

    async def _generate_openrouter(self, prompt: str, context: str) -> str:
        headers = {
            "Authorization": f"Bearer {settings.openrouter_api_key}",
            "Content-Type": "application/json",
            "HTTP-Referer": "https://localhost",
            "X-Title": "PC",
        }
        payload = {
            "model": settings.openrouter_model,
            "messages": [
                {"role": "system", "content": "Você é PC, um assistente de IA premium e prático."},
                {"role": "user", "content": f"Contexto:\n{context}\n\nPergunta:\n{prompt}"},
            ],
        }
        try:
            async with httpx.AsyncClient(timeout=30) as client:
                response = await client.post("https://openrouter.ai/api/v1/chat/completions", headers=headers, json=payload)
                response.raise_for_status()
                data = response.json()
                return data["choices"][0]["message"]["content"].strip()
        except Exception:
            return self._fallback_response(prompt, context)

    async def _generate_openai(self, prompt: str, context: str) -> str:
        headers = {"Authorization": f"Bearer {settings.openai_api_key}", "Content-Type": "application/json"}
        payload = {
            "model": settings.openai_model,
            "messages": [
                {"role": "system", "content": "Você é PC, um assistente premium."},
                {"role": "user", "content": f"Contexto:\n{context}\n\nPergunta:\n{prompt}"},
            ],
        }
        try:
            async with httpx.AsyncClient(timeout=30) as client:
                response = await client.post("https://api.openai.com/v1/chat/completions", headers=headers, json=payload)
                response.raise_for_status()
                data = response.json()
                return data["choices"][0]["message"]["content"].strip()
        except Exception:
            return self._fallback_response(prompt, context)

    async def _generate_ollama(self, prompt: str, context: str) -> str:
        payload = {
            "model": settings.ollama_model,
            "messages": [
                {"role": "system", "content": "Você é PC, um assistente premium e direto."},
                {"role": "user", "content": f"Contexto:\n{context}\n\nPergunta:\n{prompt}"},
            ],
        }
        try:
            async with httpx.AsyncClient(timeout=30) as client:
                response = await client.post(f"{settings.ollama_base_url}/api/chat", json=payload)
                response.raise_for_status()
                data = response.json()
                return data["message"]["content"].strip()
        except Exception:
            return self._fallback_response(prompt, context)

    def _fallback_response(self, prompt: str, context: str) -> str:
        lower = prompt.lower()

        if any(word in lower for word in ["pesquise", "procure", "buscar", "internet", "web", "notícia", "noticias"]):
            return "PC está pronto para pesquisar e resumir as fontes mais relevantes. Configure uma API de busca para resposta real em tempo real."

        if any(word in lower for word in ["código", "codigo", "programar", "python", "react", "app", "api", "backend", "frontend"]):
            return "Posso estruturar a solução, criar a arquitetura e montar um MVP real com código pronto para evoluir."

        if any(word in lower for word in ["roteiro", "vídeo", "video", "script", "conteúdo", "conteudo"]):
            return "Claro. Posso transformar essa ideia em roteiro estruturado, sequências, objetivos e proposta de narração." 

        if any(word in lower for word in ["lembre", "memória", "perfil", "preferência", "preferencia", "aprenda"]):
            return "Entendido. Vou registrar esse contexto e usá-lo nas próximas interações para personalizar a experiência."

        return f"PC online e pronto para ajudar. Contexto atual: {context[:220]}"

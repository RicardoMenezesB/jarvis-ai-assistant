from __future__ import annotations

import json
from typing import Any

import httpx

from app.config import settings


class SearchService:
    async def search(self, query: str) -> list[dict[str, Any]]:
        if settings.tavily_api_key:
            return await self._search_tavily(query)
        if settings.brave_api_key:
            return await self._search_brave(query)
        return self._fallback_results(query)

    async def _search_tavily(self, query: str) -> list[dict[str, Any]]:
        async with httpx.AsyncClient(timeout=25.0) as client:
            response = await client.post(
                "https://api.tavily.com/search",
                json={
                    "api_key": settings.tavily_api_key,
                    "query": query,
                    "search_depth": "basic",
                    "max_results": 5,
                },
            )
            response.raise_for_status()
            payload = response.json()
            return payload.get("results", [])

    async def _search_brave(self, query: str) -> list[dict[str, Any]]:
        async with httpx.AsyncClient(timeout=25.0) as client:
            response = await client.get(
                "https://api.search.brave.com/res/v1/web/search",
                headers={
                    "Accept": "application/json",
                    "Accept-Encoding": "gzip",
                    "X-Subscription-Token": settings.brave_api_key,
                },
                params={"q": query, "count": 5},
            )
            response.raise_for_status()
            payload = response.json()
            results = payload.get("web", {}).get("results", [])
            return [{"title": item.get("title"), "url": item.get("url"), "content": item.get("description", "")} for item in results]

    def _fallback_results(self, query: str) -> list[dict[str, Any]]:
        return [
            {
                "title": f"Resultado de referência para: {query}",
                "url": "https://example.com/search",
                "content": "Sem API de busca ativa configurada. PC pode usar este módulo quando houver integração real com Tavily ou Brave.",
            }
        ]

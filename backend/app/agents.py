from __future__ import annotations

from typing import Any

import httpx

from app.config import settings


class SearchService:
    async def search(self, query: str, limit: int = 5) -> list[dict[str, Any]]:
        if settings.tavily_api_key:
            return await self._search_tavily(query, limit)
        if settings.brave_api_key:
            return await self._search_brave(query, limit)
        return self._fallback_results(query)

    async def _search_tavily(self, query: str, limit: int) -> list[dict[str, Any]]:
        async with httpx.AsyncClient(timeout=25.0) as client:
            response = await client.post(
                "https://api.tavily.com/search",
                json={
                    "api_key": settings.tavily_api_key,
                    "query": query,
                    "search_depth": "basic",
                    "max_results": limit,
                },
            )
            response.raise_for_status()
            payload = response.json()
            return payload.get("results", [])

    async def _search_brave(self, query: str, limit: int) -> list[dict[str, Any]]:
        async with httpx.AsyncClient(timeout=25.0) as client:
            response = await client.get(
                "https://api.search.brave.com/res/v1/web/search",
                headers={
                    "Accept": "application/json",
                    "Accept-Encoding": "gzip",
                    "X-Subscription-Token": settings.brave_api_key,
                },
                params={"q": query, "count": limit},
            )
            response.raise_for_status()
            payload = response.json()
            web_results = payload.get("web", {}).get("results", [])
            return [
                {
                    "title": item.get("title"),
                    "url": item.get("url"),
                    "content": item.get("description", ""),
                }
                for item in web_results
            ]

    def _fallback_results(self, query: str) -> list[dict[str, Any]]:
        return [{
            "title": f"Referência para: {query}",
            "url": "https://example.com/search",
            "content": "Busca em tempo real ainda não configurada. Conecte Tavily ou Brave para pesquisa online real."
        }]

from __future__ import annotations

from typing import Any

from app.memory_store import MemoryStore
from app.services.llm import LLMService
from app.services.search import SearchService


class VoiceAgent:
    def __init__(self) -> None:
        self.llm = LLMService()

    async def respond(self, session_id: str, message: str, memory_store: MemoryStore) -> str:
        context = memory_store.summarize(session_id)
        return await self.llm.generate(message, context)


class ResearchAgent:
    def __init__(self) -> None:
        self.search = SearchService()

    async def run(self, query: str) -> list[dict[str, Any]]:
        return await self.search.search(query, limit=5)


class CodingAgent:
    def __init__(self) -> None:
        self.llm = LLMService()

    async def run(self, query: str, context: str) -> str:
        return await self.llm.generate(
            f"Crie uma solução prática e bem estruturada para esta demanda: {query}",
            context,
        )


class CreativeAgent:
    def __init__(self) -> None:
        self.llm = LLMService()

    async def run(self, query: str, context: str) -> str:
        return await self.llm.generate(
            f"Transforme esta ideia em roteiro ou conteúdo premium: {query}",
            context,
        )


class PlanningAgent:
    def __init__(self) -> None:
        self.llm = LLMService()

    async def run(self, query: str, context: str) -> str:
        return await self.llm.generate(
            f"Organize uma estratégia, plano de ação e prioridades para: {query}",
            context,
        )


class MemoryAgent:
    def __init__(self) -> None:
        self.llm = LLMService()

    async def run(self, query: str, context: str) -> str:
        return await self.llm.generate(
            f"Use memória e aprendizado para personalizar a resposta com base neste contexto: {query}",
            context,
        )


class AgentOrchestrator:
    def __init__(self, memory_store: MemoryStore):
        self.memory_store = memory_store
        self.voice_agent = VoiceAgent()
        self.research_agent = ResearchAgent()
        self.coding_agent = CodingAgent()
        self.creative_agent = CreativeAgent()
        self.planning_agent = PlanningAgent()
        self.memory_agent = MemoryAgent()

    async def handle(self, session_id: str, message: str) -> dict[str, Any]:
        self.memory_store.push(session_id, "user", message)
        self.memory_store.learn_preference(session_id, message)

        intent = self.detect_intent(message)
        context = self.memory_store.get_context(session_id)
        profile = self.memory_store.to_profile_summary(session_id)

        search_results: list[dict[str, Any]] = []

        if intent in {"research", "web"}:
            search_results = await self.research_agent.run(message)

        if intent == "research":
            reply = self._summarize_search(message, search_results, context, profile)
        elif intent == "coding":
            reply = await self.coding_agent.run(message, f"{context}\nPerfil: {profile}")
        elif intent == "creative":
            reply = await self.creative_agent.run(message, f"{context}\nPerfil: {profile}")
        elif intent == "planning":
            reply = await self.planning_agent.run(message, f"{context}\nPerfil: {profile}")
        elif intent == "memory":
            reply = await self.memory_agent.run(message, f"{context}\nPerfil: {profile}")
        else:
            reply = await self.voice_agent.respond(session_id, message, self.memory_store)

        self.memory_store.push(session_id, "assistant", reply)

        return {
            "intent": intent,
            "reply": reply,
            "voice": reply,
            "memory": profile,
            "context_summary": context,
            "search_results": search_results[:3],
            "suggestions": self.suggestions(intent),
        }

    def detect_intent(self, message: str) -> str:
        text = message.lower()

        if any(keyword in text for keyword in ["pesquise", "procure", "buscar", "web", "internet", "notícia", "noticias"]):
            return "research"
        if any(keyword in text for keyword in ["código", "codigo", "programar", "python", "react", "app", "api", "backend", "frontend"]):
            return "coding"
        if any(keyword in text for keyword in ["roteiro", "vídeo", "video", "script", "conteúdo", "conteudo"]):
            return "creative"
        if any(keyword in text for keyword in ["planejar", "organizar", "agenda", "semana", "meta", "objetivo"]):
            return "planning"
        if any(keyword in text for keyword in ["lembre", "memória", "perfil", "preferência", "preferencia", "aprenda"]):
            return "memory"
        return "assistant"

    def suggestions(self, intent: str) -> list[str]:
        if intent == "research":
            return ["Comparar fontes", "Gerar resumo", "Extrair conclusões"]
        if intent == "coding":
            return ["Gerar arquitetura", "Criar MVP", "Construir UI e API"]
        if intent == "creative":
            return ["Definir roteiro", "Estruturar cenas", "Ajustar tom de voz"]
        if intent == "planning":
            return ["Definir prioridades", "Criar cronograma", "Separar tarefas"]
        if intent == "memory":
            return ["Guardar preferência", "Atualizar perfil", "Lembrar estilo de resposta"]
        return ["Aprimorar contexto", "Executar ação", "Gerar plano de resposta"]

    def _summarize_search(self, query: str, results: list[dict[str, Any]], context: str, profile: str) -> str:
        if not results:
            return f"PC realizou uma busca sobre '{query}' e não encontrou resultados imediatos. Posso continuar com um resumo mais aprofundado assim que tiver fontes."

        summary_lines = [f"Busca realizada sobre: {query}"]
        for item in results[:3]:
            title = item.get("title") or "Resultado"
            content = item.get("content") or "Sem resumo disponível"
            url = item.get("url") or ""
            summary_lines.append(f"- {title}: {content[:180]}{' ...' if len(content) > 180 else ''}")
            if url:
                summary_lines.append(f"  Fonte: {url}")

        summary_lines.append(f"Contexto: {context[:200]}")
        summary_lines.append(f"Perfil: {profile}")
        return "\n".join(summary_lines)

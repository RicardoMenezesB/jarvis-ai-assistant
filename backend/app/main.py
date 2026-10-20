from __future__ import annotations

from app.memory_store import MemoryStore
from app.services.llm import LLMService
from app.services.search import SearchService


class AgentOrchestrator:
    def __init__(self, memory_store: MemoryStore):
        self.memory_store = memory_store
        self.llm = LLMService()
        self.search = SearchService()

    async def handle(self, session_id: str, message: str) -> dict:
        self.memory_store.push(session_id, "user", message)
        self.memory_store.learn_preference(session_id, message)

        intent = self._detect_intent(message)
        search_results = []

        if intent in {"research", "web", "analysis"}:
            search_results = await self.search.search(message)

        context = self.memory_store.get_context(session_id)
        memory_profile = self.memory_store.to_profile_summary(session_id)

        response = await self.llm.generate(message, f"{context}\n\nPerfil: {memory_profile}")

        self.memory_store.push(session_id, "assistant", response)

        return {
            "intent": intent,
            "reply": response,
            "voice": response,
            "memory": memory_profile,
            "context_summary": context,
            "search_results": search_results[:3],
            "suggestions": self._suggestions(intent),
        }

    def _detect_intent(self, message: str) -> str:
        lower = message.lower()

        if any(keyword in lower for keyword in ["pesquise", "procure", "web", "internet", "buscar", "notícias"]):
            return "research"
        if any(keyword in lower for keyword in ["código", "codigo", "programar", "python", "react", "api", "app"]):
            return "coding"
        if any(keyword in lower for keyword in ["roteiro", "vídeo", "video", "script", "conteúdo", "content"]):
            return "creative"
        if any(keyword in lower for keyword in ["lembre", "memória", "perfil", "me lembre", "aprenda"]):
            return "memory"
        return "assistant"

    def _suggestions(self, intent: str) -> list[str]:
        if intent == "research":
            return ["Pesquisar fontes confiáveis", "Comparar opções", "Gerar resumo executivo"]
        if intent == "coding":
            return ["Criar MVP", "Estruturar backend", "Gerar componentes UI"]
        if intent == "creative":
            return ["Gerar roteiro", "Definir tom de voz", "Organizar cenas"]
        if intent == "memory":
            return ["Salvar preferência", "Registrar objetivos", "Atualizar perfil"]
        return ["Falar mais sobre o objetivo", "Gerar plano de ação", "Transformar em execução"]

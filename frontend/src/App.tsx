from __future__ import annotations

from typing import Any

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

from app.agents import AgentOrchestrator
from app.config import settings
from app.memory_store import MemoryStore

app = FastAPI(title=settings.api_title, version=settings.api_version)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

memory_store = MemoryStore()
agent_orchestrator = AgentOrchestrator(memory_store)


class ChatRequest(BaseModel):
    message: str
    session_id: str = "pc-default-session"


class ConfigUpdate(BaseModel):
    provider: str | None = None
    groq_api_key: str | None = None
    groq_model: str | None = None
    openrouter_api_key: str | None = None
    openrouter_model: str | None = None
    openai_api_key: str | None = None
    openai_model: str | None = None
    ollama_base_url: str | None = None
    ollama_model: str | None = None
    tavily_api_key: str | None = None
    brave_api_key: str | None = None
    elevenlabs_api_key: str | None = None
    elevenlabs_voice_id: str | None = None
    azure_speech_key: str | None = None
    azure_speech_region: str | None = None


@app.get("/api/health")
async def health() -> dict[str, Any]:
    return {
        "status": "ok",
        "name": settings.app_name,
        "version": settings.api_version,
        "provider": settings.provider,
        "model": settings.selected_model(),
    }


@app.get("/api/config")
async def get_config() -> dict[str, Any]:
    return {
        "provider": settings.provider,
        "model": settings.selected_model(),
        "providers": {
            "groq": bool(settings.groq_api_key),
            "openrouter": bool(settings.openrouter_api_key),
            "openai": bool(settings.openai_api_key),
            "ollama": True,
        },
    }


@app.post("/api/config")
async def update_config(payload: ConfigUpdate) -> dict[str, Any]:
    for field_name, value in payload.model_dump().items():
        if value is None or value == "":
            continue
        if hasattr(settings, field_name):
            setattr(settings, field_name, value)

    settings.model = settings.selected_model()
    return {
        "provider": settings.provider,
        "model": settings.selected_model(),
        "status": "updated",
    }


@app.post("/api/chat")
async def chat(request: ChatRequest) -> dict[str, Any]:
    result = await agent_orchestrator.handle(request.session_id, request.message)
    return result


@app.get("/api/memory/{session_id}")
async def memory(session_id: str) -> dict[str, Any]:
    return {
        "session_id": session_id,
        "context": memory_store.get_context(session_id),
        "profile": memory_store.to_profile_summary(session_id),
    }


@app.post("/api/voice")
async def voice(request: ChatRequest) -> dict[str, Any]:
    result = await agent_orchestrator.handle(request.session_id, request.message)
    return {
        "transcript": request.message,
        "reply": result["reply"],
        "voice": result["voice"],
    }


if __name__ == "__main__":
    import uvicorn

    uvicorn.run("app.main:app", host="0.0.0.0", port=8000, reload=True)

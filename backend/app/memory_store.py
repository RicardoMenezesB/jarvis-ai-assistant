from __future__ import annotations

import os
from dataclasses import dataclass
from typing import Optional

from dotenv import load_dotenv

load_dotenv()


@dataclass
class Settings:
    app_name: str = "PC"
    api_title: str = "PC AI Assistant"
    api_version: str = "0.3.0"
    default_language: str = "pt-BR"
    app_mode: str = "development"

    provider: str = "groq"
    model: str = "llama-3.1-70b-versatile"

    groq_api_key: Optional[str] = None
    groq_model: str = "llama-3.1-70b-versatile"

    openrouter_api_key: Optional[str] = None
    openrouter_model: str = "openai/gpt-4o-mini"

    openai_api_key: Optional[str] = None
    openai_model: str = "gpt-4o-mini"

    ollama_base_url: str = "http://localhost:11434"
    ollama_model: str = "llama3.1"

    tavily_api_key: Optional[str] = None
    brave_api_key: Optional[str] = None

    elevenlabs_api_key: Optional[str] = None
    elevenlabs_voice_id: Optional[str] = None

    azure_speech_key: Optional[str] = None
    azure_speech_region: str = "eastus"

    default_session_id: str = "pc-default-session"

    def selected_model(self) -> str:
        if self.provider == "groq":
            return self.groq_model
        if self.provider == "openrouter":
            return self.openrouter_model
        if self.provider == "openai":
            return self.openai_model
        if self.provider == "ollama":
            return self.ollama_model
        return self.groq_model


settings = Settings(
    app_name=os.getenv("APP_NAME", "PC"),
    default_language=os.getenv("DEFAULT_LANGUAGE", "pt-BR"),
    app_mode=os.getenv("APP_MODE", "development"),
    provider=os.getenv("ACTIVE_PROVIDER", "groq"),
    groq_api_key=os.getenv("GROQ_API_KEY"),
    groq_model=os.getenv("GROQ_MODEL", "llama-3.1-70b-versatile"),
    openrouter_api_key=os.getenv("OPENROUTER_API_KEY"),
    openrouter_model=os.getenv("OPENROUTER_MODEL", "openai/gpt-4o-mini"),
    openai_api_key=os.getenv("OPENAI_API_KEY"),
    openai_model=os.getenv("OPENAI_MODEL", "gpt-4o-mini"),
    ollama_base_url=os.getenv("OLLAMA_BASE_URL", "http://localhost:11434"),
    ollama_model=os.getenv("OLLAMA_MODEL", "llama3.1"),
    tavily_api_key=os.getenv("TAVILY_API_KEY"),
    brave_api_key=os.getenv("BRAVE_API_KEY"),
    elevenlabs_api_key=os.getenv("ELEVENLABS_API_KEY"),
    elevenlabs_voice_id=os.getenv("ELEVENLABS_VOICE_ID"),
    azure_speech_key=os.getenv("AZURE_SPEECH_KEY"),
    azure_speech_region=os.getenv("AZURE_SPEECH_REGION", "eastus"),
)
settings.model = settings.selected_model()

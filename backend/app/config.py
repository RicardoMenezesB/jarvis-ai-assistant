from __future__ import annotations

from dataclasses import dataclass
from typing import Optional
import os

from dotenv import load_dotenv

load_dotenv()


@dataclass
class Settings:
    app_name: str = "PC"
    api_title: str = "PC AI Assistant"
    api_version: str = "0.2.0"
    groq_api_key: Optional[str] = None
    groq_model: str = "llama-3.1-70b-versatile"
    tavily_api_key: Optional[str] = None
    brave_api_key: Optional[str] = None
    default_session_id: str = "pc-default-session"


settings = Settings(
    groq_api_key=os.getenv("GROQ_API_KEY"),
    groq_model=os.getenv("GROQ_MODEL", "llama-3.1-70b-versatile"),
    tavily_api_key=os.getenv("TAVILY_API_KEY"),
    brave_api_key=os.getenv("BRAVE_API_KEY"),
)

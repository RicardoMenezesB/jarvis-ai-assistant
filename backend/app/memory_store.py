from __future__ import annotations

from collections import defaultdict, deque
from typing import Any


class MemoryStore:
    def __init__(self, max_history: int = 20):
        self.max_history = max_history
        self.sessions: dict[str, deque[str]] = defaultdict(deque)
        self.profiles: dict[str, dict[str, Any]] = defaultdict(dict)

    def push(self, session_id: str, role: str, content: str) -> None:
        history = self.sessions[session_id]
        history.append(f"{role}: {content}")
        while len(history) > self.max_history:
            history.popleft()

    def get_context(self, session_id: str) -> str:
        history = list(self.sessions.get(session_id, []))
        if not history:
            return "Sem memória recente."
        return "\n".join(history)

    def learn_preference(self, session_id: str, message: str) -> None:
        text = message.lower()
        profile = self.profiles[session_id]

        if any(phrase in text for phrase in ["prefiro", "gosto de", "quero que", "me lembre", "lembre-se", "sou"]):
            profile["last_note"] = message

        if "python" in text:
            profile["language"] = "Python"
        if "react" in text:
            profile["framework"] = "React"
        if "voz" in text or "microfone" in text:
            profile["interaction"] = "voz"
        if "premium" in text:
            profile["style"] = "premium"
        if "objetivo" in text or "meta" in text:
            profile["focus"] = "produtividade"

    def to_profile_summary(self, session_id: str) -> str:
        profile = self.profiles.get(session_id, {})
        if not profile:
            return "Nenhuma preferência memorizada ainda."
        return ", ".join(f"{key}: {value}" for key, value in profile.items())

    def summarize(self, session_id: str) -> str:
        context = self.get_context(session_id)
        profile = self.to_profile_summary(session_id)
        return f"Contexto: {context}\nPerfil: {profile}"

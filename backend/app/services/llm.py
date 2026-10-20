from __future__ import annotations

from collections import defaultdict, deque
from typing import Any


class MemoryStore:
    def __init__(self, max_history: int = 12):
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
        lower = message.lower()
        profile = self.profiles[session_id]

        for key in ["prefiro", "gosto de", "quero", "lembre-se", "me lembre"]:
            if key in lower:
                profile["last_note"] = message
                break

        if "python" in lower:
            profile["language"] = "Python"
        if "react" in lower:
            profile["framework"] = "React"
        if "voz" in lower:
            profile["interaction"] = "voz"

    def to_profile_summary(self, session_id: str) -> str:
        profile = self.profiles.get(session_id, {})
        if not profile:
            return "Nenhuma preferência memorizada ainda."
        return ", ".join(f"{k}: {v}" for k, v in profile.items())

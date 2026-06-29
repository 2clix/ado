"""Portas (interfaces) do domínio — implementadas pela infrastructure layer."""
from __future__ import annotations
from typing import Protocol
from .workitem import WorkItem


class BacklogRepository(Protocol):
    def fetch_by_query_id(self, query_id: str, project: str) -> list[WorkItem]: ...


class AIAssistant(Protocol):
    def ask(self, context: str, history: list[dict[str, str]], question: str) -> str: ...

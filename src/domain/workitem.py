"""WorkItem — entidade central do domínio. Sem dependências externas."""
from __future__ import annotations
from dataclasses import dataclass, field
from datetime import datetime, timezone


@dataclass(frozen=True)
class WorkItem:
    id: int
    title: str
    state: str
    assigned_to: str
    priority: str
    item_type: str
    changed_date: str
    created_date: str
    effort: float | None
    tags: str

    def days_since_change(self) -> int | None:
        if not self.changed_date:
            return None
        try:
            dt = datetime.fromisoformat(self.changed_date.replace("Z", "+00:00"))
            return (datetime.now(timezone.utc) - dt).days
        except ValueError:
            return None

    def is_blocked(self) -> bool:
        state = self.state.lower()
        return any(k in state for k in ("reprovado", "bloqueado", "duplicado"))

    def is_done(self) -> bool:
        state = self.state.lower()
        return any(k in state for k in ("done", "publicado", "validado qa", "pronto para qa"))

    def is_active(self) -> bool:
        state = self.state.lower()
        return any(k in state for k in ("andamento", "executar", "fazendo"))

    def is_stale(self, threshold_days: int = 3) -> bool:
        days = self.days_since_change()
        return days is not None and days > threshold_days

    def is_critical(self) -> bool:
        return self.priority in ("0", "1")

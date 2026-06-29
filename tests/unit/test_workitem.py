"""Testes de unidade para o WorkItem — sem dependências externas."""
from src.domain.workitem import WorkItem


def _make(state: str = "Em andamento", priority: str = "2", changed_date: str = "") -> WorkItem:
    return WorkItem(
        id=1,
        title="Test item",
        state=state,
        assigned_to="Dev",
        priority=priority,
        item_type="User Story",
        changed_date=changed_date,
        created_date="2026-01-01T00:00:00Z",
        effort=None,
        tags="",
    )


def test_is_blocked_reprovado():
    assert _make(state="Reprovado").is_blocked() is True


def test_is_blocked_em_andamento():
    assert _make(state="Em andamento").is_blocked() is False


def test_is_done_publicado():
    assert _make(state="Publicado").is_done() is True


def test_is_done_em_andamento():
    assert _make(state="Em andamento").is_done() is False


def test_is_active():
    assert _make(state="Em andamento").is_active() is True
    assert _make(state="Para executar").is_active() is True
    assert _make(state="Done").is_active() is False


def test_is_critical():
    assert _make(priority="0").is_critical() is True
    assert _make(priority="1").is_critical() is True
    assert _make(priority="2").is_critical() is False


def test_days_since_change_no_date():
    assert _make(changed_date="").days_since_change() is None

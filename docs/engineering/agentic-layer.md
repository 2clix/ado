---
name: agentic-layer
description: Mapa de rules/agents/skills/workflows. Puxe ao evoluir a camada agêntica.
alwaysApply: false
---

# Camada agêntica do projeto

Quatro tipos de artefato, todos versionados — gerados/propostos pelo `/kickoff` e evoluídos ao
longo do projeto.

## 1. Rules — como o agente deve se comportar
- **`CLAUDE.md`** — convenções, stack Python, quality gates, Definition of Done. Lido em toda sessão.
- **`.claude/settings.json`** — permissões (allowlist dos comandos Python, pytest, ruff, mypy,
  bandit) e **hooks** (`SessionStart` → `load-context.sh`).

## 2. Docs — o conhecimento (a constituição)
vision · mvp-canvas · design · domain · spec · ADRs · glossary · context-map · roadmap.
A spec continua sendo a **fonte da verdade**.

## 3. Agents (subagentes) — especialistas sob demanda
`.claude/agents/<nome>.md`. Exemplos típicos para Python + IA:
- **`spec-reviewer`** — valida critérios de aceite testáveis (gate *Definition of Ready*).
- **`domain-modeler`** — extrai linguagem ubíqua e agregados de uma spec; checa o glossário.
- **`adr-writer`** — rascunha um ADR a partir de uma decisão.
- **`pytest-tester`** — roda e interpreta os testes do projeto.
- **`claude-api-advisor`** — consultor de uso da API Anthropic (modelos, pricing, tool use).

## 4. Skills — workflows reutilizáveis
`.claude/skills/<nome>/SKILL.md`:

| Skill | Responsabilidade |
|---|---|
| **`/kickoff`** | orquestra a constituição (Lean Inception + 5 eixos + geração) |
| **`/mapear`** | brownfield as-is → `assessment.md` |
| **`/diagramar`** | arquitetura de alto nível em Mermaid → `diagrams.md` |
| **`/roadmap`** | constrói/revisa o roadmap com o time |
| **`/camada-agentica`** | propõe/gera rules, subagents, skills, workflows/CI |
| **`/integracoes`** | ferramentas do time + MCPs (ortogonal ao kickoff) |
| **`/nova-feature`** | loop por feature (tier → spec → tasks) |
| **`/clarificar`** | sabatina implacável para fechar ambiguidade antes de codar |
| **`/validar`** | UAT local: gates, AC→teste, SPEC_DEVIATION, DoD |
| **`/revisar-pr`** | gate de conformidade SDD no PR |
| **`/setup-ci`** | pipeline CI/CD que materializa os gates SDD |
| **`/metricas`** | Lead Time · Throughput · maturidade de CD |
| **`/auditar`** | valida conformidade da esteira (frontmatter, links, rastreabilidade) |
| **`/evals`** | fidelidade spec→código (AC por task/teste, SPEC_DEVIATION) |
| **`/handoff`** | pausa/retoma via `docs/STATE.md` |

## 5. Workflows — automação da esteira
- **Hooks** (`settings.json`): `SessionStart` → `.claude/hooks/load-context.sh`
- **CI/CD** (`/setup-ci`): falhar PR sem spec aprovada; rodar testes de aceite.
- **Gate de PR** (`/revisar-pr`): conformidade de processo.
- **Conformidade da esteira** (`.github/workflows/esteira.yml`): valida frontmatter e specs.

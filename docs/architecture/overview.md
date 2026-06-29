---
name: architecture-overview
description: Arquitetura do sistema nos 5 eixos + segurança e operacional. Puxe ao trabalhar em arquitetura, infra, qualidade, observabilidade ou segurança.
alwaysApply: false
---

# Arquitetura do sistema

> Visão **consolidada** do sistema pelos 5 eixos (+ segurança e operacional). Cada seção é um
> **resumo curto + link** para o detalhe (ADRs, context-map, diagrams, TESTING). Gerado/atualizado
> no `/kickoff`. **Mantenha enxuto** — o detalhe vive nos docs linkados, aqui é o mapa.

## 1. Tech stack
- **Linguagem:** Python 3.11+
- **Gerenciador:** pip / uv
- **Testes:** pytest + pytest-cov
- **Lint:** ruff
- **Type check:** mypy
- **SAST:** bandit
- **SDK IA:** anthropic (claude-sonnet-4-6)
- **HTTP ADO:** urllib (stdlib) — sem dependência extra
- Decisão: _a preencher via `/kickoff`_ → ADR-0001

## 2. Arquitetura base
- Monolito modular em camadas DDD
- Camadas: `domain/` ← `application/` ← `infrastructure/`, `interfaces/`
- Bounded contexts: _a mapear via `/kickoff`_
- Mapa de contextos: [context-map.md](context-map.md) · Diagramas: [diagrams.md](diagrams.md)
- Decisão: _a registrar_ → ADR-0002

## 3. Infra
- Execução local (CLI) — sem servidor
- Deploy: nenhum por ora (script CLI)
- Segredos via variáveis de ambiente (`ADO_PAT`, `ANTHROPIC_API_KEY`)
- Decisão: _a registrar_ → ADR-0003

## 4. Qualidade
- Pirâmide: unit (domínio) > integration (adapters) > acceptance (CLI ponta-a-ponta)
- Cobertura mínima: 80%
- Lint/format limpos, mypy sem erros, bandit sem achados médios/altos
- Comandos e gates: [TESTING.md](../engineering/TESTING.md)

## 5. Observabilidade
- Logs estruturados: _a definir_ (hoje: print simples)
- Métricas: _nenhuma por ora_
- Decisão: _a registrar_ → ADR-0004

## 6. Segurança
- PAT do ADO e API key Anthropic **nunca hardcoded** — variáveis de ambiente
- SAST via bandit no CI
- _Revisão de segurança: a realizar via `/security-review`_

## 7. Operacional
- CLI local; sem SLA formal por ora
- Runbook: _a criar_

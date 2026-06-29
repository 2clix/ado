---
name: adr-0001
description: Primeira ADR — decisão de registrar decisões via ADR.
alwaysApply: false
---

# ADR-0001: Registrar decisões arquiteturais com ADR

- **Status:** aceito
- **Data:** 2026-06-29
- **Decisores:** Rafael Baena

## Contexto
À medida que o projeto cresce de um script único (`backlog.py`) para uma arquitetura modular
Python + IA, decisões de design tornam-se mais frequentes e difíceis de rastrear. Sem registro
formal, o "porquê" de escolhas se perde, dificultando onboarding e revisão.

## Decisão
Vamos registrar toda decisão arquitetural difícil de reverter como um ADR numerado em
`docs/architecture/adr/`. Cada ADR é imutável — se uma decisão mudar, cria-se um novo ADR
que substitui o anterior.

## Consequências
- **+** Rastreabilidade histórica das decisões; facilita onboarding
- **+** Força reflexão antes de decisões estruturais
- **−** Overhead de escrever o doc (mitigado pelo template e pela skill `/kickoff`)

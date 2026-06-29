---
name: STATE
description: Memória de trabalho volátil — onde paramos, próximo passo, bloqueios.
alwaysApply: true
---

# STATE — Memória viva do projeto

> Memória de trabalho **entre sessões** (humanos e agentes). É **volátil**: atualizada o tempo
> todo. Diferente do **ADR** (decisão durável e imutável). Decisão estrutural → ADR; estado do
> trabalho → aqui. Atualize ao **pausar/encerrar**; leia ao **retomar**. Use a skill `/handoff`.

**Última atualização:** 2026-06-29 por Rafael Baena

## Em andamento / próximo passo
> O que está aberto agora e a **próxima ação concreta** (não "continuar a feature" — diga o passo).
- Projeto inicializado com boilerplate SDD (spec-driven)
- Próximo passo: rodar `/kickoff` para preencher vision.md, context-map.md, ADRs e roadmap

## Decisões recentes
> Resumo cronológico. Se for difícil de reverter, vire um ADR e linke aqui.
- 2026-06-29: Adotado boilerplate SDD (spec-driven) para organizar o desenvolvimento Python + IA

## Bloqueios
- [ ] _nenhum bloqueio no momento_

## Ideias adiadas / backlog técnico
- Migrar `backlog.py` monolítico para arquitetura em camadas DDD (quando houver spec aprovada)
- Avaliar uso de `rich` para CLI mais elegante
- Considerar cache local das queries ADO para reduzir latência

## Todos soltos
- [ ] Rodar `/kickoff` para preencher os artefatos de produto e arquitetura
- [ ] Rodar `/integracoes` para mapear Azure DevOps + Anthropic como MCPs
- [ ] Definir estrutura de testes (`pytest`) para `backlog.py`

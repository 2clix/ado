---
name: integrations
description: Ferramentas do time e MCPs conectados. Puxe ao integrar ou verificar fluxos de leitura/escrita.
alwaysApply: false
---

# Integrações e MCPs

> Gerado/atualizado pela skill `/integracoes`. Fonte única das ferramentas e conexões validadas.

## Ferramentas do time

| Ferramenta | Categoria | MCP server | Conta/workspace validada | Status |
|------------|-----------|------------|--------------------------|--------|
| Azure DevOps | Gestão/processo | _a conectar_ | — | pendente |
| Anthropic API | IA | direto via SDK | — | em uso (backlog.py) |

## Fluxos de leitura (read-first)
- ADO: queries WIQL → WorkItems (já implementado em `backlog.py`)
- Anthropic: contexto de backlog → resposta Claude (já implementado em `backlog.py`)

## Fluxos de escrita (write-side)
- _a definir via `/integracoes`_

## MCPs configurados
- _nenhum ainda — rode `/integracoes` para conectar_

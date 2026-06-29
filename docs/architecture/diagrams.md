---
name: diagrams
description: Diagramas de arquitetura em Mermaid (C4 L1/L2 + context map). Puxe ao visualizar a arquitetura. Gere/atualize com /diagramar.
alwaysApply: false
---

# Diagramas de Arquitetura

> Gerado/atualizado com a skill `/diagramar`. Mantenha **alto nível** — sem detalhe de implementação.

## Contexto do sistema (C4 L1)

```mermaid
flowchart TD
    RB["Rafael Baena\n(Gestão Dev)"]
    CLI["2clix Backlog CLI\n(Python)"]
    ADO["Azure DevOps\n(sistema externo)"]
    CLAUDE["Anthropic Claude API\n(sistema externo)"]

    RB -->|usa| CLI
    CLI -->|consulta WorkItems via WIQL| ADO
    CLI -->|envia contexto e pergunta| CLAUDE
    CLAUDE -->|resposta em linguagem natural| CLI
```

## Containers (C4 L2)

> _A preencher via `/diagramar` após o kickoff._

## Mapa de bounded contexts (DDD)

```mermaid
flowchart LR
    ADO_CTX["Integrações ADO\n(generic)"]
    BACKLOG["Backlog\n(core)"]
    REL["Relatórios\n(supporting)"]
    IA["Assistente IA\n(supporting)"]

    ADO_CTX -->|Customer/Supplier| BACKLOG
    BACKLOG -->|Conformist| REL
    BACKLOG -->|ACL| IA
```

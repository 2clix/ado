---
name: src
description: Regra de camadas DDD. Puxe ao estruturar ou implementar código Python.
alwaysApply: false
---

# src/ — Estrutura em camadas (DDD tático) — Python

A dependência aponta **só para dentro**:

```
interfaces ──► application ──► domain ◄── infrastructure
```

| Camada            | Pasta                   | Responsabilidade                                          | Pode depender de              |
|-------------------|-------------------------|-----------------------------------------------------------|-------------------------------|
| `domain/`         | `src/domain/`           | Entidades, value objects, eventos, regras/invariantes     | **nada** (sem framework/IO)   |
| `application/`    | `src/application/`      | Casos de uso, orquestração, portas (interfaces/protocols) | `domain/`                     |
| `infrastructure/` | `src/infrastructure/`   | Adapters ADO, Anthropic SDK, HTTP, repos concretos        | `domain/`, `application/`     |
| `interfaces/`     | `src/interfaces/`       | CLI (argparse/rich), handlers de entrada, formatação      | `application/`                |

## Convenções Python

- `domain/`: apenas `@dataclass`, `Protocol`, lógica pura. Nenhum `import` de lib externa.
- `application/`: `Protocol` para portas, implementação dos casos de uso.
- `infrastructure/`: `AzureDevOpsClient`, `AnthropicClient`, implementações de repos.
- `interfaces/`: `cli.py`, formatação colorida, menus — sem lógica de negócio.
- Cada módulo tem `__init__.py`. Exports explícitos.

## Exemplo de estrutura
```
src/
├── domain/
│   ├── __init__.py
│   ├── workitem.py        # WorkItem dataclass, regras de negócio
│   └── ports.py           # Protocols (interfaces) para repos e clients
├── application/
│   ├── __init__.py
│   └── backlog_service.py # Casos de uso: buscar, filtrar, analisar
├── infrastructure/
│   ├── __init__.py
│   ├── ado_client.py      # Adapter Azure DevOps (HTTP)
│   └── claude_client.py   # Adapter Anthropic SDK
└── interfaces/
    ├── __init__.py
    └── cli.py             # Comandos CLI, formatação, menu
```

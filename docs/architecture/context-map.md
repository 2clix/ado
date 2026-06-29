---
name: context-map
description: Bounded contexts e relações. Puxe ao modelar ou cruzar contextos.
alwaysApply: false
---

# Context Map

> Visão DDD estratégica: os bounded contexts do sistema e como se relacionam.
> Atualize quando uma feature cria/move fronteiras. Combine com diagramas C4 se útil.

## Bounded Contexts
| Contexto          | Subdomínio          | Responsabilidade                            | Dono     |
|-------------------|---------------------|---------------------------------------------|----------|
| Backlog           | core                | Consulta e análise de WorkItems do ADO      | Rafael   |
| Relatórios        | supporting          | Geração de relatórios (daily, jornal, etc.) | Rafael   |
| Assistente IA     | supporting          | Chat em linguagem natural via Claude        | Rafael   |
| Integrações ADO   | generic             | Autenticação e requisições ao Azure DevOps  | —        |

## Relações entre contextos

```
[Backlog] ──(Customer/Supplier)──► [Integrações ADO]
[Relatórios] ──(Conformist)──► [Backlog]
[Assistente IA] ──(ACL)──► [Backlog]
```

| Upstream          | Downstream       | Padrão              | Por quê |
|-------------------|------------------|---------------------|---------|
| Integrações ADO   | Backlog           | Customer/Supplier   | ADO é fonte de dados externa; backlog consome via adapter |
| Backlog           | Relatórios        | Conformist          | Relatórios consomem o modelo do Backlog sem transformar |
| Backlog           | Assistente IA     | Anti-Corruption Layer | Claude recebe texto plano; ACL isola o modelo de domínio |

## Diagramas
Os diagramas de arquitetura de alto nível ficam em [`diagrams.md`](./diagrams.md) — gere/atualize com a skill `/diagramar`.

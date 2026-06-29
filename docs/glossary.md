---
name: glossary
description: Linguagem ubíqua. Puxe ao nomear, modelar domínio ou escrever specs.
alwaysApply: false
---

# Glossário — Linguagem Ubíqua

> A fonte única do vocabulário do sistema. O mesmo termo aparece aqui, na spec e no código.
> Termo novo introduzido por uma feature → adicione no mesmo PR. Sem sinônimos.

| Termo              | Definição                                                        | NÃO confundir com      | Contexto          |
|--------------------|------------------------------------------------------------------|------------------------|-------------------|
| WorkItem           | Unidade de trabalho rastreável no Azure DevOps (User Story, Bug, Task) | ticket (evitar)   | ADO               |
| Esteira            | Conjunto de queries ADO que representa uma fila de entrega de um papel/time | pipeline (diferente) | Backlog     |
| Query              | Consulta WIQL salva no ADO que retorna uma lista de WorkItems     | relatório              | ADO               |
| Assignee           | Pessoa responsável por um WorkItem no momento                    | dono permanente        | ADO               |
| Daily              | Reunião diária de acompanhamento; no sistema, o relatório gerado para ela | stand-up        | Processo          |
| Gargalo            | WorkItem parado há mais dias que o limiar, ou pessoa com WIP acima do normal | bloqueio (mais específico) | Métricas |
| Bloqueio           | WorkItem em estado "Reprovado" ou "Bloqueado"                    | gargalo                | ADO               |
| WIP                | Work In Progress — quantidade de itens ativos por pessoa         | throughput             | Métricas          |
| Jornal             | Relatório semanal de demandas do projeto                         | daily                  | Relatórios        |
| Claude             | Modelo de IA da Anthropic usado no comando `ask` e em agentes    | GPT, LLM (genérico)    | IA                |
| PAT                | Personal Access Token do Azure DevOps usado para autenticação    | senha, token OAuth     | Segurança         |

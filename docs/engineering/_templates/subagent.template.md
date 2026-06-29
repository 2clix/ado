---
name: subagent-template
description: Template para criar um subagente especialista. Use ao propor via /camada-agentica.
alwaysApply: false
---

# Subagente: <nome>

> Arquivo: `.claude/agents/<nome>.md`
> Especialista sob demanda — recebe task + contexto mínimo, devolve report-back estruturado.

## Responsabilidade
<Uma frase: o que este subagente faz e quando é acionado.>

## Contexto de entrada esperado
- `spec.md` da feature ativa
- `docs/engineering/TESTING.md` (para subagentes de teste)
- <outros docs específicos>

## Saída esperada
<Formato do report-back: tabela de resultados, lista de findings, veredicto go/no-go, etc.>

## Limitações
- Não lê o repo inteiro — recebe só o necessário
- Não toma decisões arquiteturais (reporta e aguarda confirmação)

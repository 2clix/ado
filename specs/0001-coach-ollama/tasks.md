---
name: tasks
description: Decomposição da feature coach-ollama. Puxe ao implementar.
alwaysApply: false
---

# Tasks — Agile Coach via Ollama

## Plano

| #  | Task                                                         | Cobre AC      | Depende de | Gate                                               | Status |
|----|--------------------------------------------------------------|---------------|------------|----------------------------------------------------|--------|
| 1  | Constantes `OLLAMA_HOST`, `OLLAMA_MODEL` + `ollama_generate()` | AC-4, AC-5  | —          | `python3 -c "from backlog import ollama_generate"` | todo   |
| 2  | `build_team_snapshot(data)` — serializa estado do backlog   | AC-2, AC-3    | —          | retorna dict com devs + métricas sem chamar API    | todo   |
| 3  | Prompt para recomendação por dev                             | AC-2          | 1, 2       | output contém nome de cada dev                     | todo   |
| 4  | Prompt para previsão de risco do sprint                      | AC-3          | 1, 2       | output contém BAIXO / MÉDIO / ALTO                 | todo   |
| 5  | `cmd_coach(data)` — orquestra 1–4, formata output           | AC-1, AC-2, AC-3 | 1–4    | `python3 backlog.py coach` exibe coach completo    | todo   |
| 6  | Registrar `coach` no MENU e no entry point                   | AC-1          | 5          | opção `0. coach` aparece no menu interativo        | todo   |

> Tasks 1 e 2 são independentes — podem ser implementadas em paralelo `[P]`.

## Contexto técnico

**Ollama REST API** (sem dependência externa — usa `urllib`):

```
POST http://localhost:11434/api/generate
Content-Type: application/json

{"model": "qwen2.5-coder:14b", "prompt": "...", "stream": false}

→ {"response": "...", "done": true}
```

**Snapshot mínimo por dev** (entrada do LLM):
```json
{
  "nome": "Danilo Plasicov",
  "papel": "Back ★",
  "em_andamento": 2,
  "bloqueados": 1,
  "parados_5d": 1,
  "finalizados_7d": 3,
  "incidentes": 0,
  "items": ["#48562 BUG usuario_ia não consegue...", "..."]
}
```

**Prompt de recomendação por dev** (template):
```
Você é um agile coach experiente. Analise o estado de trabalho do dev abaixo e escreva
uma recomendação em português de 1 a 3 linhas. Seja direto, construtivo e específico.
Não invente dados além dos fornecidos. Use tom profissional mas humano.

Dev: {nome} ({papel})
Em andamento: {em_andamento} | Bloqueados: {bloqueados} | Parados >5d: {parados_5d}
Finalizados (7d): {finalizados_7d} | Incidentes: {incidentes}
Items: {items}

Recomendação:
```

**Prompt de previsão do sprint**:
```
Você é um agile coach. Com base no snapshot do time abaixo, avalie o risco de entrega
do sprint. Responda em português com:
1. Nível de risco: BAIXO, MÉDIO ou ALTO
2. Até 4 fatores de risco identificados
3. Uma ação recomendada para o Scrum Master

Snapshot:
{snapshot_resumo}
```

## Plano de teste

- **Unidade:** `build_team_snapshot(data)` com `data` mockado — valida shape do dict
- **Integração:** `ollama_generate("ping")` — requer Ollama rodando localmente
- **Aceite:** `python3 backlog.py coach` — exercita AC-1 a AC-5 manualmente

## Divergências (SPEC_DEVIATION)

- [ ] nenhuma no momento

## Checklist de Definition of Done

- [ ] AC-1 a AC-5 verificados manualmente (Ollama rodando + backlog carregado)
- [ ] AC-4 verificado com Ollama parado (`ollama stop`)
- [ ] `OLLAMA_HOST` e `OLLAMA_MODEL` documentados em `.env.example`
- [ ] `coach` aparece no help da CLI e no menu interativo
- [ ] Nenhum `SPEC_DEVIATION` pendente
- [ ] `docs/STATE.md` atualizado

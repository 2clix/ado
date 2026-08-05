---
name: spec
description: Contrato da feature coach-ollama. Base enquanto a feature está ativa.
alwaysApply: true
---

# Spec — Agile Coach via Ollama

> **Fonte da verdade.** Status: aprovado
> Os critérios de aceite são o contrato com o negócio e o oráculo de teste.

## Resumo

O comando `coach` carrega o estado atual do backlog, monta um snapshot do time e chama
um modelo LLM local via Ollama para gerar (1) uma recomendação por desenvolvedor e
(2) uma previsão de risco de entrega do sprint.

## Critérios de aceite

### AC-1: Comando `coach` disponível na CLI e no menu

- **Dado** que o usuário executa `python3 backlog.py coach` ou seleciona a opção no menu interativo
- **Quando** o comando é executado com Ollama disponível
- **Então** o output exibe o cabeçalho `🤖 Agile Coach · <modelo> · <data>` e as seções
  de recomendação por dev e previsão do sprint

### AC-2: Recomendação por desenvolvedor

- **Dado** que o backlog foi carregado (via cache ou fetch)
- **Quando** o coach processa o time
- **Então** para cada pessoa em `DEVS + INTEGRACOES + QA_DEVS + GESTAO` o output exibe:
  - nome e papel
  - uma recomendação de 1–3 linhas em português (foco, risco ou parabéns)
  - nenhuma informação inventada além do contexto fornecido

### AC-3: Previsão de risco de entrega do sprint

- **Dado** o snapshot do backlog (WIP, bloqueados, parados, P0/P1)
- **Quando** o LLM processa os dados
- **Então** o output exibe:
  - nível de risco: `BAIXO` / `MÉDIO` / `ALTO`
  - 2–4 fatores de risco identificados em português
  - uma ação recomendada para o Scrum Master

### AC-4: Fallback quando Ollama está offline

- **Dado** que `OLLAMA_HOST` não está acessível (connection refused ou timeout)
- **Quando** `coach` é executado
- **Então** o CLI exibe a mensagem `⚠ Ollama não encontrado em <host>. Inicie com: ollama serve`
  e encerra com exit code 1 sem stack trace

### AC-5: Configuração via variáveis de ambiente

- **Dado** que as variáveis `OLLAMA_HOST` e/ou `OLLAMA_MODEL` estão definidas no `.env`
- **Quando** `coach` é executado
- **Então** usa os valores das variáveis (defaults: `http://localhost:11434`, `qwen2.5`)

## Matriz de decisão

| Ollama acessível | Dados carregados | Resultado | AC |
|---|---|---|---|
| Sim | Sim (cache ou live) | Exibe coach completo | AC-1, AC-2, AC-3 |
| Não | qualquer | Mensagem de fallback, exit 1 | AC-4 |
| Sim | Vazio (0 items) | Exibe aviso "Sem dados de backlog" | AC-1 |

## Casos de borda e erros

- Timeout na chamada Ollama (> 60 s): exibe `⚠ Timeout ao chamar Ollama` e encerra
- Resposta do modelo vazia ou malformada: exibe o texto cru sem formatação extra
- Dev sem items no backlog: exibe `Sem itens ativos — nada a reportar`

## Fora de escopo

- Histórico de sessões de coach (cada execução é stateless)
- Comparação entre dias / sprints
- Substituir o comando `ask` existente (Anthropic)
- Fine-tuning ou configuração de parâmetros do modelo além de `model` e `host`
- Suporte a stream de resposta (output incremental)

## Rastreabilidade

- ADRs relacionados: [ADR-0002](../../docs/architecture/adr/0002-stdlib-http.md) — stdlib HTTP (urllib) mantida para a chamada Ollama

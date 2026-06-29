#!/usr/bin/env bash
# Hook SessionStart — injeta o contexto base SDD (docs alwaysApply: true) no início da sessão.
# O stdout deste script é adicionado ao contexto do Claude Code.
# Roda a partir da raiz do projeto; lê só o que existe.

BASE_DOCS=(
  "docs/STATE.md"
  "docs/product/vision.md"
  "docs/product/roadmap.md"
)

echo "# Contexto base SDD (carregado no SessionStart)"
echo "> Estes são os docs \`alwaysApply: true\`. Os demais são sob demanda — puxe pelo \`description\`."

any=0
for f in "${BASE_DOCS[@]}"; do
  if [ -f "$f" ]; then
    echo ""
    echo "===== $f ====="
    cat "$f"
    any=1
  fi
done

echo ""
echo "> Spec da feature ativa: veja \"Em andamento\" no STATE e leia \`specs/NNNN-*/spec.md\`."

#!/bin/bash
# Overnight experiment chain: N → O → P → Q → R → S → T
# Pace: 35s between messages (~8-9 hours for 813 turns)
# Resumes automatically from last checkpoint if interrupted.

set -e
cd "$(dirname "$0")"

PACE=35
NOMI="e07268e6-61f9-47d0-bd19-502c6c0a4ef1"

echo "=== Overnight run starting: $(date) ==="
echo "Experiments: N O P Q R S T | Pace: ${PACE}s | Nomi: ${NOMI}"
echo ""

run_exp() {
  local exp=$1
  echo "--- Starting Experiment $exp: $(date) ---"
  NOMI_API_KEY="${NOMI_API_KEY}" python3 runner.py "experiments/${exp}" --nomi "$NOMI" --pace "$PACE"
  echo "--- Finished Experiment $exp: $(date) ---"
  echo ""
}

run_exp N-emotional-weight.yaml
run_exp O-unresolved-threads.yaml
run_exp P-identity-attack.yaml
run_exp Q-forget-this.yaml
run_exp R-emotional-state-continuity.yaml
run_exp S-forgetting-curve-fine.yaml
run_exp T-category-assignment.yaml

echo "=== All experiments complete: $(date) ==="

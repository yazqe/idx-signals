#!/usr/bin/env bash
# Direct one-shot LLM call to the local MLX backend via the headroom proxy (:8799).
# Replaces `hermes -z` for the batch Hermes pipeline: the agent harness (system
# prompt + tools + skills) drives Qwen3-Next-80B into reasoning-only/empty
# responses. A plain completion call returns the markdown directly and reliably.
# Usage: llm_oneshot.sh "<prompt>"  -> prints model content to stdout.
set -euo pipefail

PROMPT="$1"
ENDPOINT="${LLM_ENDPOINT:-http://127.0.0.1:8799/v1/chat/completions}"
MAX_TOKENS="${LLM_MAX_TOKENS:-4000}"

REQ=$(python3 -c "import json,sys;print(json.dumps({'model':'base','messages':[{'role':'user','content':sys.argv[1]}],'max_tokens':int(sys.argv[2])}))" "$PROMPT" "$MAX_TOKENS")

RESP=$(printf '%s' "$REQ" | curl -s -m 240 -X POST "$ENDPOINT" -H 'Content-Type: application/json' -d @-)

printf '%s' "$RESP" | python3 -c "
import json, sys
try:
    d = json.load(sys.stdin)
    c = (d['choices'][0]['message']['content'] or '').strip()
except Exception as e:
    sys.stderr.write('llm_oneshot: bad response: %s\n' % e)
    sys.exit(1)
if not c:
    sys.stderr.write('llm_oneshot: empty content\n')
    sys.exit(1)
sys.stdout.write(c + '\n')
"

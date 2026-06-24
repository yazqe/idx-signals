#!/usr/bin/env bash
# Auto-sync ~/.hermes/config.yaml → repo backup (hermes-config.yaml.bak).
# ~/.hermes is not a git repo, so this snapshots its config into idx-signals on
# every change. Triggered by launchd WatchPaths (com.yazqe.hermes-config-sync).
# No-ops when the file is unchanged (WatchPaths can fire on metadata too).
set -euo pipefail

SRC="$HOME/.hermes/config.yaml"
ROOT="$HOME/idx-signals"
DST="$ROOT/hermes-config.yaml.bak"

[ -f "$SRC" ] || exit 0
cmp -s "$SRC" "$DST" && exit 0   # unchanged → nothing to do

cp "$SRC" "$DST"
cd "$ROOT"
git add hermes-config.yaml.bak
git commit -q -m "Auto-sync hermes config.yaml backup ($(date '+%Y-%m-%d %H:%M'))" || exit 0
git pull -q --rebase --autostash origin main || true   # avoid non-fast-forward vs daily.sh pushes
git push -q || true

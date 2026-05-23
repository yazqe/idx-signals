#!/usr/bin/env bash
# Helper to discover Telegram channel chat_id after adding bot as admin.
# Run: ./setup_telegram.sh
set -euo pipefail

if [ -z "${TELEGRAM_BOT_TOKEN:-}" ]; then
  echo "TELEGRAM_BOT_TOKEN not set. Export it first:"
  echo '  export TELEGRAM_BOT_TOKEN="123456:ABC..."'
  exit 1
fi

echo "Polling getUpdates from Telegram..."
RESPONSE=$(curl -s "https://api.telegram.org/bot${TELEGRAM_BOT_TOKEN}/getUpdates")

if ! echo "$RESPONSE" | jq -e '.ok' > /dev/null 2>&1; then
  echo "API error:"
  echo "$RESPONSE" | jq . 2>/dev/null || echo "$RESPONSE"
  exit 1
fi

echo ""
echo "All chats the bot knows about:"
echo "$RESPONSE" | jq -r '
  .result[]
  | (.channel_post.chat // .message.chat // .my_chat_member.chat // empty)
  | "  \(.type | ascii_upcase | (. + (" " * (8 - length))))  id=\(.id)  title=\(.title // .username // "(no title)")"
' | sort -u

echo ""
echo "Next: pick the channel id (starts with -100...) and run:"
echo "  export TELEGRAM_CHAT_ID='-1001234567890'"
echo "  echo 'export TELEGRAM_CHAT_ID=\"-1001234567890\"' >> ~/.zshrc"
echo ""
echo "Then test:"
echo "  curl -s -X POST \"https://api.telegram.org/bot\${TELEGRAM_BOT_TOKEN}/sendMessage\" \\"
echo "    -d chat_id=\"\${TELEGRAM_CHAT_ID}\" -d text='✅ idx-signals connected'"

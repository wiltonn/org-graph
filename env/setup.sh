
#!/usr/bin/env bash
set -euo pipefail
corepack enable || true
pnpm i
echo "Dev env ready."

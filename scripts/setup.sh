#!/usr/bin/env bash
source ~/code/website/env/bin/activate
cd website/
set -o allexport; source ~/code/website/.dev; set +o allexport
npm run build </dev/null &>/dev/null &
npm run start </dev/null &>/dev/null &
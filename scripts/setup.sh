#!/usr/bin/env bash
. ./env/bin/activate
set -o allexport; source ~/code/website/.env; set +o allexport
cd website/

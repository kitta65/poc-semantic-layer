#!/bin/bash
set -euo pipefail
cd "$(dirname "$0")"/..

rm -rf .env

{
  echo "UID=$(id -u)"
  echo "GID=$(id -g)"

  echo "CUBEJS_DB_BQ_PROJECT_ID=$(gcloud config get project)"
  echo "CUBEJS_DB_BQ_CREDENTIALS=$(cat "${HOME}/.config/gcloud/application_default_credentials.json" | base64 | tr -d '\n')"
} >> .env

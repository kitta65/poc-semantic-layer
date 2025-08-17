#!/bin/bash
set -euo pipefail
cd "$(dirname "$0")"

rm -rf cube/.env
touch cube/.env

{
  echo "CUBEJS_DB_TYPE=bigquery"
  echo "CUBEJS_DB_BQ_PROJECT_ID=$(gcloud config get project)"
  echo "CUBEJS_DB_BQ_CREDENTIALS=$(cat "${HOME}/.config/gcloud/application_default_credentials.json" | base64 | tr -d '\n')"

  # TODO: check if these configs are needed
  # CUBEJS_API_SECRET=SUPERSECRET
  # CUBEJS_EXTERNAL_DEFAULT=true
  # CUBEJS_SCHEDULED_REFRESH_DEFAULT=true
  # CUBEJS_DEV_MODE=true
  # CUBEJS_SCHEMA_PATH=model
} >> cube/.env

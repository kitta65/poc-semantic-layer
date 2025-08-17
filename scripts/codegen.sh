#!/bin/bash
set -euo pipefail
cd "$(dirname "$0")"/..

tempfile=/tmp/schema.json

uv run python -m sgqlc.introspection http://localhost:4000/cubejs-api/graphql $tempfile
uv run sgqlc-codegen schema $tempfile schema.py

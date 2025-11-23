#!/bin/bash

# --- Variables ---

SCRIPT_DIR=$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" &> /dev/null && pwd)
BASE_DIR="$(dirname -- "${SCRIPT_DIR}")"
CONFIG_DIR="$BASE_DIR/config"
NEWS_API_KEY=$(cat "$CONFIG_DIR/.env" | grep NEWS_API_KEY | grep -oP '=\K\w+')

# --- Main Script ---
curl "https://newsapi.org/v2/everything?q=bitcoin&apiKey=$NEWS_API_KEY"
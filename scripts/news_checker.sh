#!/bin/bash

# ==============================================================================
# SCRIPT SETTINGS
# ==============================================================================
set -o nounset
set -o errexit
set -o pipefail

# ==============================================================================
# DIRECTORY VARIABLES
# ==============================================================================
SCRIPT_DIR=$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" &> /dev/null && pwd)
BASE_DIR="$(dirname -- "${SCRIPT_DIR}")"
CONFIG_DIR="$BASE_DIR/config"
DATA_DIR="$BASE_DIR/data"

# ==============================================================================
# CONFIG OTHER VARIABLES
# ==============================================================================
TIMESTAMP=$(date +"%Y-%m-%d_%H-%M-%S")
NEWS_API_KEY=$(cat "$CONFIG_DIR/.env" | grep NEWS_API_KEY | grep -oP '=\K\w+')
QUERY="(Trump or US GOVERN) AND (crypto OR cryptocurrency OR bitcoin)"

# ==============================================================================
# MAIN EXECUTION
# ==============================================================================
curl "https://newsapi.org/v2/everything?q=$QUERY&apiKey=$NEWS_API_KEY" >> "$date '+%Y%m%d%H%M%S'"
#!/bin/bash

# ==============================================================================
# SCRIPT SETTINGS
# ==============================================================================
set -o nounset
set -o errexit
set -o pipefail

# ==============================================================================
# PATH VARIABLES
# ==============================================================================
SCRIPT_DIR=$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" &> /dev/null && pwd)
BASE_DIR="$(dirname -- "${SCRIPT_DIR}")"
CONFIG_DIR="$BASE_DIR/config"
DATA_DIR="$BASE_DIR/data"
RAW_DATA_DIR="$DATA_DIR/raw"
CLEANED_DATA_DIR="$DATA_DIR/cleaned"
LOG_DIR="$BASE_DIR/log"

# ==============================================================================
# CONFIG OTHER VARIABLES
# ==============================================================================
TIMESTAMP=$(date +"%Y-%m-%d_%H-%M-%S")
LOG_FILE="${LOG_DIR}/${TIMESTAMP}.log"
ERR_FILE="${LOG_DIR}/${TIMESTAMP}.err"
NEWS_API_KEY=$(cat "$CONFIG_DIR/.env" | grep NEWS_API_KEY | grep -oP '=\K\w+')
API_BASE_URL="https://newsapi.org/v2/everything?"

# ==============================================================================
# QUERY CONSTRUCTION
# ==============================================================================
AGENCIES=(SEC OR CFTC OR FinCEN OR IRS OR OCC OR Treasury OR Federal Reserve)
MARKETS=(Crypto OR Digital Assets OR Cryptocurrency)
PRODUCTS=(Bitcoin OR Ethereum OR Stablecoin OR DeFi OR NFT OR Cryptocurrency OR Custody OR KYC/AML OR blockchain)
ACTIONS=(Enforcement Action OR Lawsuit OR Unregistered Security OR Fraud)
RULES=(Regulation OR Framework OR Guidance OR Clarity Act OR Legislation OR Genius Act)
ACTORS=(Trump OR US Government OR US OR United States OR America OR Congress OR Senate OR House of Representatives)

QUERY="((${AGENCIES[*]}) OR (${ACTORS[*]})) AND ((${MARKETS[*]}) OR (${PRODUCTS[*]})) AND ((${ACTIONS[*]}) OR (${RULES[*]}))"

# ==============================================================================
# REDIRECT OUTPUTS TO LOG FILES
# ==============================================================================
exec > >(tee -a "${LOG_FILE}")
exec 2> >(tee -a "${ERR_FILE}" >&2)

# ==============================================================================
# MAIN EXECUTION
# ==============================================================================
echo "$TIMESTAMP - $SCRIPT_DIR/news_checker.sh" >> "$CONFIG_DIR/news_checker_path.log"

curl -s --get "$API_BASE_URL" \
     --data-urlencode "q=$QUERY" \
     --data-urlencode "apiKey=$NEWS_API_KEY" >> "$RAW_DATA_DIR/$TIMESTAMP.txt"
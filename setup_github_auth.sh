#!/bin/bash

echo "=================================================="
echo "      Ezrex AI Bot - Secure GitHub Auth Setup     "
echo "=================================================="

# Prompt for GitHub Username
read -p "Enter your GitHub Username: " GH_USER

# Prompt for Repository Name
read -p "Enter your Repository Name (e.g., school-of-tech): " GH_REPO

# Securely prompt for Personal Access Token (hidden input)
read -s -p "Enter your GitHub Personal Access Token (PAT): " GH_TOKEN
echo ""

if [ -z "$GH_TOKEN" ] || [ -z "$GH_USER" ] || [ -z "$GH_REPO" ]; then
    echo "❌ Error: Inputs cannot be empty!"
    exit 1
fi

# Save to hidden .env file
cat << ENV_EOF > .env
GH_USER="$GH_USER"
GH_REPO="$GH_REPO"
GH_TOKEN="$GH_TOKEN"
ENV_EOF

chmod 600 .env
echo "✅ Credentials securely saved to hidden .env file!"

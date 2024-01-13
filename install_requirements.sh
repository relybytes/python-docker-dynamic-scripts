#!/bin/bash

# Check if OS_ADDITIONAL_PACKAGES is set and not empty
if [ -n "$OS_ADDITIONAL_PACKAGES" ]; then
    apt-get update
    apt-get install -y $OS_ADDITIONAL_PACKAGES
fi

# Read the requirements from the environment variable and install
echo "$PIP_REQUIREMENTS" > requirements.txt
pip install --root-user-action=ignore --no-cache-dir -r requirements.txt

# Execute your Python script
exec python -u execute.py

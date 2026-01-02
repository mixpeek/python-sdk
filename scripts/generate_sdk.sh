#!/bin/bash
# Generate Mixpeek Python SDK from root OpenAPI spec
# This script should be run from the python-client directory

set -e  # Exit on error

# Colors for output
GREEN='\033[0;32m'
BLUE='\033[0;34m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

echo -e "${BLUE}=== Mixpeek Python SDK Generator ===${NC}"

# Determine script and repo directories
SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
SDK_DIR="$(dirname "$SCRIPT_DIR")"
# Go up from sdk/python-client/scripts to server root
SERVER_ROOT="$(cd "$SDK_DIR/../.." && pwd)"
OPENAPI_SPEC="$SERVER_ROOT/openapi.json"

echo -e "${BLUE}SDK Directory: $SDK_DIR${NC}"
echo -e "${BLUE}Server Root: $SERVER_ROOT${NC}"
echo -e "${BLUE}OpenAPI Spec: $OPENAPI_SPEC${NC}"

# Verify OpenAPI spec exists
if [ ! -f "$OPENAPI_SPEC" ]; then
    echo -e "${YELLOW}Error: OpenAPI spec not found at $OPENAPI_SPEC${NC}"
    exit 1
fi

# Check if openapi-python-client is installed
if ! command -v openapi-python-client &> /dev/null; then
    echo -e "${YELLOW}openapi-python-client not found. Installing...${NC}"
    pip install openapi-python-client pyyaml
fi

# Navigate to SDK directory
cd "$SDK_DIR"

# Backup existing mixpeek package if it exists
if [ -d "mixpeek" ]; then
    echo -e "${BLUE}Backing up existing mixpeek package...${NC}"
    rm -rf mixpeek.backup
    cp -r mixpeek mixpeek.backup
fi

# Generate the SDK
echo -e "${BLUE}Generating SDK from OpenAPI spec...${NC}"
openapi-python-client generate \
    --path "$OPENAPI_SPEC" \
    --config openapi-config.yml \
    --overwrite

# Apply custom overrides
if [ -f "scripts/apply_overrides.py" ]; then
    echo -e "${BLUE}Applying SDK configuration overrides...${NC}"
    python scripts/apply_overrides.py
fi

# Clean up backup if generation was successful
if [ -d "mixpeek.backup" ]; then
    echo -e "${BLUE}Removing backup...${NC}"
    rm -rf mixpeek.backup
fi

echo -e "${GREEN}✓ SDK generation complete!${NC}"
echo -e "${BLUE}Next steps:${NC}"
echo -e "  1. Review generated code in ./mixpeek/"
echo -e "  2. Run tests: python test.py"
echo -e "  3. Build package: python setup.py sdist bdist_wheel"

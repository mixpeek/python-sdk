# Setup Guide for Automated SDK Publishing

This guide will help you set up the automated SDK generation and publishing pipeline.

## Overview

The Python SDK is automatically:
1. Generated from the OpenAPI specification at `https://server-xb24.onrender.com/docs/openapi.json`
2. Published to PyPI when the API version changes
3. Tagged and released on GitHub

## Prerequisites

- GitHub account with access to both `mixpeek/server` and `mixpeek/python-sdk` repositories
- PyPI account with API token
- npm installed (for openapi-generator-cli)

## Step 1: Set Up PyPI

### 1.1 Create a PyPI Account

1. Go to [pypi.org](https://pypi.org) and create an account
2. Verify your email address

### 1.2 Generate API Token

1. Go to [pypi.org/manage/account/token/](https://pypi.org/manage/account/token/)
2. Click "Add API token"
3. Name it: `mixpeek-python-sdk`
4. Scope: Select "Project: mixpeek" (or "Entire account" if the project doesn't exist yet)
5. Click "Add token"
6. **IMPORTANT**: Copy the token immediately (it starts with `pypi-`)

### 1.3 Add Token to GitHub Secrets

1. Go to the `mixpeek/python-sdk` repository on GitHub
2. Navigate to: **Settings → Secrets and variables → Actions**
3. Click "New repository secret"
4. Name: `PYPI_API_TOKEN`
5. Value: Paste the PyPI token you copied
6. Click "Add secret"

## Step 2: Set Up GitHub Personal Access Token (PAT)

### 2.1 Create a Fine-Grained PAT

1. Go to GitHub: **Settings → Developer settings → Personal access tokens → Fine-grained tokens**
2. Click "Generate new token"
3. Configure:
   - **Token name**: `mixpeek-sdk-trigger`
   - **Expiration**: 1 year (or your preference)
   - **Repository access**: Only select repositories
     - Select: `mixpeek/python-sdk`
   - **Repository permissions**:
     - Contents: Read and write
     - Actions: Read and write
     - Workflows: Read and write
4. Click "Generate token"
5. **IMPORTANT**: Copy the token immediately (starts with `github_pat_`)

### 2.2 Add PAT to Server Repository

1. Go to the `mixpeek/server` repository on GitHub
2. Navigate to: **Settings → Secrets and variables → Actions**
3. Click "New repository secret"
4. Name: `SDK_TRIGGER_TOKEN`
5. Value: Paste the PAT you copied
6. Click "Add secret"

## Step 3: Add Workflow to Server Repository

Create a file at `.github/workflows/trigger-sdk-update.yml` in the **server repository**:

```yaml
name: Trigger SDK Update

on:
  push:
    branches:
      - main
    paths:
      - 'app/**'              # Adjust to your API code path
      - 'openapi.json'        # If you have a static OpenAPI file
  
  # Manual trigger
  workflow_dispatch:

jobs:
  trigger-sdk-generation:
    runs-on: ubuntu-latest
    
    steps:
      - name: Trigger Python SDK Update
        run: |
          curl -X POST \
            -H "Accept: application/vnd.github.v3+json" \
            -H "Authorization: token ${{ secrets.SDK_TRIGGER_TOKEN }}" \
            https://api.github.com/repos/mixpeek/python-sdk/dispatches \
            -d '{"event_type":"openapi-update"}'
      
      - name: Notify
        run: |
          echo "✅ Triggered Python SDK regeneration"
```

## Step 4: Test the Pipeline

### Manual Test (Recommended First)

1. Go to the `mixpeek/python-sdk` repository
2. Navigate to: **Actions → Sync OpenAPI and Publish to PyPI**
3. Click "Run workflow" dropdown
4. Select branch: `main`
5. Click "Run workflow"
6. Watch the workflow run and verify it completes successfully

### Automatic Test

1. Make a small change to your server API code
2. Commit and push to the `main` branch of `mixpeek/server`
3. Check the Actions tab in both repositories:
   - `mixpeek/server`: Should show "Trigger SDK Update" workflow
   - `mixpeek/python-sdk`: Should show "Sync OpenAPI and Publish to PyPI" workflow
4. After completion, check:
   - [PyPI](https://pypi.org/project/mixpeek/) for the new version
   - [GitHub Releases](https://github.com/mixpeek/python-sdk/releases) for the new tag

## How It Works

### Workflow Trigger Flow

```
Server Repo (main branch)
    ↓
  Push to main
    ↓
GitHub Actions: trigger-sdk-update.yml
    ↓
Repository Dispatch Event
    ↓
Python SDK Repo
    ↓
GitHub Actions: sync-and-publish.yml
    ↓
1. Download OpenAPI spec
2. Extract version
3. Check if version exists on PyPI
4. Generate SDK (if new version)
5. Build package
6. Publish to PyPI
7. Create GitHub Release
```

### Version Management

- The version is automatically extracted from the OpenAPI spec's `info.version` field
- If the version already exists on PyPI, the workflow skips publishing
- To publish a new version, update the version in your OpenAPI spec

## Local Development

### Generate SDK Locally

```bash
# Clone the repository
git clone https://github.com/mixpeek/python-sdk.git
cd python-sdk

# Run the generation script
./generate.sh
```

### Test Locally

```bash
# Install in development mode
pip install -e .

# Run tests
python -m pytest test/

# Test imports
python -c "import mixpeek; print(mixpeek.__version__)"
```

### Build and Test Package Locally

```bash
# Build the package
python -m build

# Test installation from local wheel
pip install dist/mixpeek-*.whl

# Verify
python -c "import mixpeek; print('✅ SDK installed successfully')"
```

## Troubleshooting

### Issue: "Version already exists on PyPI"

**Solution**: The workflow automatically skips publishing if the version exists. Update the version in your OpenAPI spec.

### Issue: "Authentication failed for PyPI"

**Solution**: 
1. Verify the `PYPI_API_TOKEN` secret is correctly set
2. Regenerate the token on PyPI if needed
3. Update the secret in GitHub

### Issue: "Repository dispatch not triggering"

**Solution**:
1. Verify the `SDK_TRIGGER_TOKEN` has correct permissions
2. Check the token hasn't expired
3. Verify the repository name in the curl command is correct

### Issue: "SDK generation fails"

**Solution**:
1. Check the OpenAPI spec is valid JSON
2. Verify the OpenAPI spec URL is accessible
3. Look at the workflow logs for specific errors

### Issue: "Build fails"

**Solution**:
1. Check Python syntax in generated code
2. Verify all dependencies are listed in requirements.txt
3. Check for linting errors

## Monitoring

### Check Workflow Status

- **Server Repo**: [Actions](https://github.com/mixpeek/server/actions)
- **Python SDK Repo**: [Actions](https://github.com/mixpeek/python-sdk/actions)

### Check PyPI

- **Package Page**: [pypi.org/project/mixpeek/](https://pypi.org/project/mixpeek/)
- **Download Stats**: Available on PyPI package page

### Check GitHub Releases

- [github.com/mixpeek/python-sdk/releases](https://github.com/mixpeek/python-sdk/releases)

## Updating the Pipeline

### Modify Generation Settings

Edit `.github/workflows/sync-and-publish.yml` in the python-sdk repository:

```yaml
# Change generator settings
openapi-generator-cli generate \
  -i openapi-cleaned.json \
  -g python \
  --additional-properties=packageVersion=$VERSION,...
```

### Add More Trigger Events

Edit `.github/workflows/trigger-sdk-update.yml` in the server repository:

```yaml
on:
  push:
    branches:
      - main
      - develop  # Add more branches
  release:
    types: [published]  # Trigger on release
```

## Best Practices

1. **Version Bumping**: Always bump the version in your OpenAPI spec when making API changes
2. **Semantic Versioning**: Follow [semver](https://semver.org/) for version numbers
3. **Testing**: Test the SDK locally before relying on auto-publish
4. **Documentation**: Update API documentation when adding new endpoints
5. **Breaking Changes**: Use major version bumps for breaking changes

## Support

For issues with:
- **Setup**: Check this guide or open an issue on GitHub
- **SDK Generation**: Check OpenAPI spec validity
- **Publishing**: Verify PyPI token and permissions
- **Automation**: Check GitHub Actions logs

---

Last Updated: October 2025


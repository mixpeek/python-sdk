# Setup Instructions for mixpeek/server Repository

To enable automatic SDK generation and publishing when you push to the `mixpeek/server` repository, you need to add a GitHub Actions workflow to that repository.

## Step 1: Create GitHub Personal Access Token (PAT)

1. Go to GitHub Settings → Developer settings → Personal access tokens → Fine-grained tokens
2. Click "Generate new token"
3. Configure the token:
   - **Name**: `SDK_GENERATION_TOKEN`
   - **Repository access**: Select "Only select repositories" → Choose `mixpeek/mixpeek-python`
   - **Permissions**:
     - Repository permissions:
       - Actions: Read and write
       - Contents: Read and write
4. Click "Generate token" and **copy the token**

## Step 2: Add Token to Server Repository Secrets

1. Go to `mixpeek/server` → Settings → Secrets and variables → Actions
2. Click "New repository secret"
3. Name: `SDK_REPO_TOKEN`
4. Value: Paste the PAT token you created in Step 1
5. Click "Add secret"

## Step 3: Add Workflow to mixpeek/server

Create this file in your `mixpeek/server` repository:

**File: `.github/workflows/trigger-sdk-generation.yml`**

```yaml
name: Trigger SDK Generation

on:
  push:
    branches:
      - main
      - master
    paths:
      # Only trigger when API-related files change
      - 'app/**'
      - 'api/**'
      - 'routes/**'
      - 'openapi.json'
      # Add other paths that affect your OpenAPI spec

  # Allow manual trigger for testing
  workflow_dispatch:

jobs:
  trigger-sdk:
    runs-on: ubuntu-latest
    steps:
      - name: Trigger SDK Generation
        run: |
          curl -X POST \
            -H "Accept: application/vnd.github.v3+json" \
            -H "Authorization: token ${{ secrets.SDK_REPO_TOKEN }}" \
            https://api.github.com/repos/mixpeek/mixpeek-python/dispatches \
            -d '{"event_type":"api-updated"}'

      - name: Notify
        run: |
          echo "✅ SDK generation triggered successfully"
          echo "Check progress at: https://github.com/mixpeek/mixpeek-python/actions"
```

## Step 4: Customize Trigger Paths (Optional)

Edit the `paths:` section in the workflow to match your server repository structure. Only trigger SDK generation when files that affect your API change.

## Step 5: Test the Setup

1. Make a small change to your API in `mixpeek/server`
2. Commit and push to the main/master branch
3. Check the Actions tab in both repositories:
   - `mixpeek/server` should show "Trigger SDK Generation" workflow
   - `mixpeek/mixpeek-python` should show "Generate SDK and Publish to PyPI" workflow
4. Wait for the SDK to be generated and published to PyPI (usually 3-5 minutes)

## Manual Trigger

You can also manually trigger SDK generation:

### From mixpeek/server:
Go to Actions → Trigger SDK Generation → Run workflow

### From mixpeek/mixpeek-python:
Go to Actions → Generate SDK and Publish to PyPI → Run workflow

## Troubleshooting

### SDK generation doesn't trigger
- Verify the PAT token has correct permissions
- Check that the token is added to server repository secrets as `SDK_REPO_TOKEN`
- Ensure the repository names in the curl command match exactly

### Build fails
- Check the workflow logs in mixpeek/mixpeek-python Actions tab
- Verify `PYPI_API_TOKEN` secret is set in mixpeek/mixpeek-python
- Ensure the OpenAPI spec is accessible at https://api.mixpeek.com/docs/openapi.json

### Version conflicts on PyPI
- The workflow uses `skip-existing: true` so it won't fail if the version already exists
- Version is auto-incremented on each run
- Check setup.py to see the current version number

## Architecture

```
┌─────────────────────┐
│  mixpeek/server     │
│                     │
│  Push to main ──────┼──┐
└─────────────────────┘  │
                         │ repository_dispatch
                         │ event: api-updated
                         ▼
┌─────────────────────────────────────┐
│  mixpeek/mixpeek-python             │
│                                     │
│  1. Fetch OpenAPI spec              │
│  2. Generate SDK code               │
│  3. Apply overrides (sdk-config.yml)│
│  4. Auto-increment version          │
│  5. Commit & tag                    │
│  6. Build package                   │
│  7. Publish to PyPI ────────────────┼──► PyPI
└─────────────────────────────────────┘
```

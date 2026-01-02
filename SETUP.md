# Python SDK Setup Instructions

## Quick Setup Checklist

### 1. Create GitHub Personal Access Token (PAT)

1. Go to GitHub → Settings → Developer settings → Personal access tokens → Tokens (classic)
2. Click "Generate new token (classic)"
3. Give it a name like "Python SDK Sync"
4. Select scopes:
   - ✅ `repo` (Full control of private repositories)
5. Click "Generate token"
6. **Copy the token** (you won't see it again!)

### 2. Add Secret to Server Repository

1. Go to your server repo: `https://github.com/mixpeek/showcase/settings/secrets/actions`
2. Click "New repository secret"
3. Name: `PYTHON_SDK_PAT`
4. Value: Paste the PAT you just created
5. Click "Add secret"

### 3. Test the Workflow

#### Option A: Make a test change to openapi.json
```bash
# In server repo
cd /Users/ethan/Dev/mixpeek/server

# Make any small change to trigger the workflow
touch openapi.json  # Update timestamp
git add openapi.json
git commit -m "test: trigger SDK sync"
git push origin main
```

#### Option B: Manually trigger the workflow
1. Go to `https://github.com/mixpeek/showcase/actions`
2. Click on "Sync Python SDK" workflow
3. Click "Run workflow" dropdown
4. Select branch (main)
5. Click "Run workflow" button

### 4. Verify the Sync

1. Check the Actions tab: `https://github.com/mixpeek/showcase/actions`
2. You should see a "Sync Python SDK" run in progress
3. Once complete, check the python-sdk repo: `https://github.com/mixpeek/python-sdk/commits/main`
4. You should see a new commit from `github-actions[bot]`

## How It Works

```
┌─────────────────────┐
│  Server Repo        │
│  (mixpeek/showcase) │
│                     │
│  1. Developer       │
│     updates API     │
│                     │
│  2. Commits         │
│     openapi.json    │
│                     │
│  3. Pushes to main  │
└──────────┬──────────┘
           │
           │ GitHub detects change
           ▼
┌─────────────────────┐
│  GitHub Action      │
│  sync-python-sdk    │
│                     │
│  - Checks out both  │
│    repositories     │
│  - Copies spec      │
│  - Regenerates SDK  │
│  - Commits changes  │
└──────────┬──────────┘
           │
           │ Pushes to python-sdk
           ▼
┌─────────────────────┐
│  Python SDK Repo    │
│  (mixpeek/python-   │
│   sdk)              │
│                     │
│  Updated SDK code   │
│  ready to publish   │
└─────────────────────┘
```

## Workflow Configuration Options

The workflow file is at [.github/workflows/sync-python-sdk.yml](../../.github/workflows/sync-python-sdk.yml)

### Direct Push (Current Default)
SDK changes are automatically committed and pushed to the `main` branch.

**Pros:**
- Immediate updates
- No manual intervention needed
- Simple workflow

**Cons:**
- No review before changes go live
- Potential for broken SDK to reach main

### Pull Request Mode (Optional)
To enable PR mode instead of direct push:

1. Edit `.github/workflows/sync-python-sdk.yml`
2. Find this line:
   ```yaml
   if: steps.check_changes.outputs.changes == 'true' && false
   ```
3. Change `false` to `true`:
   ```yaml
   if: steps.check_changes.outputs.changes == 'true' && true
   ```
4. Comment out or remove the "Commit and push changes" step

**Pros:**
- Review changes before merging
- Run tests in PR
- Safer for production

**Cons:**
- Requires manual PR approval
- SDK updates delayed until merge

## Troubleshooting

### Workflow fails with "Permission denied"
- Ensure `PYTHON_SDK_PAT` secret is set correctly
- Verify the PAT has `repo` scope
- Check that the PAT hasn't expired

### Workflow doesn't trigger
- Ensure the workflow file is on the `main` branch
- Check that `openapi.json` is in the root of the repository
- Verify Actions are enabled in repository settings

### SDK generation fails
- Check the action logs for detailed errors
- Test locally: `cd sdk/python-client && bash scripts/generate_sdk.sh`
- Verify `openapi.json` is valid JSON

### Changes not appearing in python-sdk repo
- Check if there were actual changes to the generated code
- Verify the "Check for changes" step detected changes
- Look at the action logs for git status output

## Manual Sync (Fallback)

If the GitHub Action isn't working, you can manually sync:

```bash
# 1. Copy openapi.json from server to python-sdk
cp /Users/ethan/Dev/mixpeek/server/openapi.json \
   /Users/ethan/Dev/mixpeek/server/sdk/python-client/openapi.json

# 2. Regenerate SDK
cd /Users/ethan/Dev/mixpeek/server/sdk/python-client
bash scripts/generate_sdk.sh

# 3. Commit and push
git add .
git commit -m "chore: regenerate SDK from OpenAPI spec"
git push origin main
```

## Next Steps

After setup is complete:

1. ✅ Verify the workflow runs successfully
2. 📝 Document your API changes in the python-sdk repo
3. 🔢 Update version in `setup.py` when ready to publish
4. 📦 Publish to PyPI: `twine upload dist/*`

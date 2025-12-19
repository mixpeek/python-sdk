# Setting up Repository Dispatch Trigger

To enable automatic SDK regeneration when the server repository pushes changes, add this workflow to your **server repository** at `.github/workflows/trigger-sdk-update.yml`:

```yaml
name: Trigger SDK Update

on:
  push:
    branches:
      - main
    paths:
      - 'app/**'  # Adjust to your API code path
      - 'openapi.json'  # If you have a static OpenAPI file

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
```

## Setup Instructions:

1. **Create a Personal Access Token (PAT)**:
   - Go to GitHub Settings → Developer settings → Personal access tokens → Fine-grained tokens
   - Create a new token with:
     - Repository access: Only select `mixpeek/python-sdk`
     - Permissions: `Contents` (Read and write) and `Actions` (Read and write)

2. **Add Secret to Server Repo**:
   - Go to `mixpeek/server` repository
   - Settings → Secrets and variables → Actions
   - Add new repository secret: `SDK_TRIGGER_TOKEN` with your PAT

3. **Add PyPI Token to Python SDK Repo**:
   - Create a PyPI API token at https://pypi.org/manage/account/token/
   - Go to `mixpeek/python-sdk` repository
   - Settings → Secrets and variables → Actions
   - Add new repository secret: `PYPI_API_TOKEN` with your PyPI token

Now, whenever you push to the server repo, it will automatically:
1. Trigger the python-sdk workflow
2. Download the latest OpenAPI spec
3. Generate the SDK
4. Publish to PyPI if the version changed
5. Create a GitHub release


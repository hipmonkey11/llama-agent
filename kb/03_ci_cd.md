
***

### `kb/ci_cd.md`
```markdown
# CI/CD Pipeline (Dummy)

## Overview
This is a **dummy CI/CD guide** describing how builds, tests, and deployments are automated.

## CI Pipeline

Typical CI steps:
1. Checkout source code.
2. Restore dependencies.
3. Build solution.
4. Run unit tests.
5. Publish artifacts.

Example pseudo-pipeline:

```yaml
# .github/workflows/ci.yml (example)
name: CI

on: [push, pull_request]

jobs:
  build:
    runs-on: windows-latest
    steps:
      - uses: actions/checkout@v4
      - name: Setup .NET
        uses: actions/setup-dotnet@v4
        with:
          dotnet-version: 8.0.x
      - name: Restore
        run: dotnet restore
      - name: Build
        run: dotnet build --configuration Release --no-restore
      - name: Test
        run: dotnet test --no-build --verbosity normal

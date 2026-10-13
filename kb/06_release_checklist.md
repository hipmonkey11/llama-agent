
***

### `kb/release_checklist.md`
```markdown
# Release Checklist (Dummy)

## Pre-Release

1. Verify that all features for this release are merged into `develop`.
2. Ensure CI pipeline is green (build and tests).
3. Update version numbers in:
   - `Directory.Build.props` or equivalent
   - Release notes / changelog

## Create Release Branch

```bash
git checkout develop
git pull
git checkout -b release/vX.Y.Z
git push -u origin release/vX.Y.Z

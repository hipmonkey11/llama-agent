
***

### `kb/test_data.md`
```markdown
# Test Data Refresh (Dummy)

## Overview
This is a **dummy test data** document describing how to refresh and manage test data.

## Daily Refresh Flow

1. Backup current test database.
2. Drop and recreate the test database.
3. Apply migrations.
4. Seed baseline data.

Example commands:

```bash
# Backup (example only)
sqlcmd -S . -Q "BACKUP DATABASE [CpBankTest] TO DISK='C:\\Backups\\CpBankTest.bak'"

# Drop & recreate via EF
dotnet ef database drop --project src/Infrastructure --force
dotnet ef database update --project src/Infrastructure

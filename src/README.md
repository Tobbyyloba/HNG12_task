# Public API for HNG12 Project

This API provides JSON responses with:

- Your registered email on the HNG12 Slack workspace.
- The current date and time in ISO 8601 format.
- The GitHub repository URL.

## Endpoint

### `GET /`
Returns:
```json
{
  "slack_email": "your-email@example.com",
  "current_datetime": "2025-01-30T12:00:00Z",
  "github_repo_url": "https://github.com/your-username/your-repository"
}

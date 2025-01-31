# Public API for HNG12 Project

This API provides JSON responses with:

- Your registered email on the HNG12 Slack workspace.
- The current date and time in ISO 8601 format.
- The GitHub repository URL.

## How to run the project locally
## Running the Project Locally

Follow these steps to set up and run the project on your local machine:

### 1. Clone the Repository
```sh
git clone <your-github-repo-url>
cd <your-project-folder>

### 2. Install Dependencies
pip install -r requirements.txt

### 3 Run App
python hng12.py

### 5 Access APi
http://127.0.0.1:5000


## Baclink
- https://hng.tech/hire/python-developers
## API Documentation

## Endpoint

### `GET https://web-production-0f26d.up.railway.app//`
Returns:
```json
{
  "slack_email": "your-email@example.com",
  "current_datetime": "2025-01-30T12:00:00Z",
  "github_repo_url": "https://github.com/your-username/your-repository"
}



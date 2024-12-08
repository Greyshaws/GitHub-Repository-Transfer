# GitHub Repository Transfer Tool

## Overview

This Python script allows you to transfer a repository from one organization or user to another on GitHub. It uses the GitHub API to initiate the transfer process and handles different response statuses to give you informative feedback on the transfer's success or failure.

This tool is ideal for automating repository management tasks and can be extended for more advanced automation workflows.

## Features

- **Transfer repositories** between organizations or from an organization to a user.
- **Command-line interface** for easy usage.
- **Informative output** for success or error handling.

## Requirements

Before using the script, ensure you have the following installed:

- **Python 3.x**: The script is compatible with Python 3.6 and higher.
- **Requests Library**: For making HTTP requests to the GitHub API.

You can install the `requests` library by running:

```bash
pip install requests
```

## Setup

### 1. Clone the Repository

Clone this repository to your local machine:

```bash
git clone <repository-url>
cd <repository-directory>
```

### 2. Generate a GitHub API Token

Generate a GitHub API token with the following permissions:

- **`repo`**: For full control of private repositories (needed to transfer repositories).

You can create a token from [GitHub Developer Settings](https://github.com/settings/tokens).

---

### 3. Running the Script

Execute the script with the required arguments:

```bash
python transfer_repo.py -k <API_TOKEN> -o <SOURCE_ORG> -r <REPO_NAME> -n <NEW_OWNER>
```

### Command-line Arguments

- **`-k`, `--api-key`** : Your GitHub API token.
- **`-o`, `--source-org`** : The organization or user currently owning the repository.
- **`-r`, `--repo-name`** : The name of the repository to transfer.
- **`-n`, `--new-owner`** : The user or organization to transfer the repository to.

### Example Command

```bash
python transfer_repo.py -k ghp_1234567890abcdef -o old-org -r example-repo -n new-owner
```

## How It Works

### 1. Input Parameters
The script accepts the following command-line arguments:

- **API Key**: The GitHub API token with repository transfer permissions.
- **Source Organization**: The organization or user currently owning the repository.
- **Repository Name**: The name of the repository to transfer.
- **New Owner**: The user or organization to transfer the repository to.

### 2. API Request
The script sends a **POST** request to the GitHub API endpoint for repository transfers.

### 3. Response Handling

- **Success (`202`)**: Transfer initiated successfully.

- **Permission Error (`403`)**: Insufficient permissions for the API token.

- **Not Found (`404`)**: The repository or organization was not found.

- **Other Errors**: Provides the HTTP status code and response message for debugging.

## Example Output

* **Successful Transfer:**
  
```
Initiating transfer of repository 'example-repo' from 'old-org' to 'new-owner'...
Repository 'example-repo' transfer initiated successfully.
```

* **Permission Error:**
  
```
Error: You do not have permission to transfer this repository.
```

* **Repository Not Found:**
  
```
Error: Repository 'example-repo' not found in organization 'old-org'.
```

## Troubleshooting

- **403 Error**: Ensure your API token has the correct permissions (`repo`).

- **404 Error**: Verify the repository name and organization are correct.

- **Network Issues**: Ensure you have a stable internet connection.


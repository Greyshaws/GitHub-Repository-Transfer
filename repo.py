import requests

# GitHub API Base URL
GITHUB_API_URL = "https://api.github.com"

def transfer_repository(api_key, source_org, repo_name, new_owner):
    """
    Transfers a repository from one organization to another user/organization.

    Args:
        api_key (str): GitHub API token with repository transfer permissions.
        source_org (str): Source organization name.
        repo_name (str): Name of the repository to transfer.
        new_owner (str): The new owner of the repository.
    """
    headers = {
        "Authorization": f"token {api_key}",
        "Accept": "application/vnd.github.v3+json"
    }

    # Transfer repository endpoint
    transfer_url = f"{GITHUB_API_URL}/repos/{source_org}/{repo_name}/transfer"

    # Data for the transfer request
    transfer_data = {
        "new_owner": new_owner
    }

    print(f"Initiating transfer of repository '{repo_name}' from '{source_org}' to '{new_owner}'...")
    response = requests.post(transfer_url, headers=headers, json=transfer_data)

    # Handle response
    if response.status_code == 202:
        print(f"Repository '{repo_name}' transfer initiated successfully.")
    elif response.status_code == 403:
        print("Error: You do not have permission to transfer this repository.")
    elif response.status_code == 404:
        print(f"Error: Repository '{repo_name}' not found in organization '{source_org}'.")
    else:
        print(f"Error: Failed to transfer repository. {response.status_code} - {response.json()}")

if __name__ == "__main__":
    import argparse

    # Command-line argument parsing
    parser = argparse.ArgumentParser(description="Transfer a repository between organizations or to a user's account.")
    parser.add_argument("-k", "--api-key", required=True, help="GitHub API token with repository transfer permissions.")
    parser.add_argument("-o", "--source-org", required=True, help="Source organization owning the repository.")
    parser.add_argument("-r", "--repo-name", required=True, help="Name of the repository to transfer.")
    parser.add_argument("-n", "--new-owner", required=True, help="New owner of the repository (user or organization).")

    args = parser.parse_args()

    # Transfer the repository
    transfer_repository(args.api_key, args.source_org, args.repo_name, args.new_owner)

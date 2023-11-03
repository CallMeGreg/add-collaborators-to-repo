**Note**: This organization uses the entitlements repo to grant access, therefore this action is not usable.

# Overview
A GitHub Action to add outside collaborators to a repository.

# Setup
Ensure that there is a GitHub App installed on the organization that has the following permissions:
- Repository permissions: Administration (read and write), Metadata (read-only)

Add two Actions secrets to the repository with the following information:
1. `APP_ID`: The App ID of the GitHub App
2. `PRIVATE_KEY`: The private key of the GitHub App

# Usage
Navigate to the `Actions` tab, then select `Add outside collaborators to a repo` from the list of workflows. Click `Run workflow` and enter the following information:
- `Collaborators`: A comma-separated list of GitHub usernames to add as collaborators
- `Repository`: The name of the repository to add collaborators to
- `Permission`: The permission level to grant to the collaborators (read, triage, write, maintain, admin)
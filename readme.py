import requests
import os
import base64

# 'skupperproject' is the name of the GitHub organization
ORG_NAME = 'skupperproject'
API_URL = f"https://api.github.com/orgs/{ORG_NAME}/repos"

def download_readme(repo):
    """
    Download the README file for a given repository.
    """
    readme_url = f"{repo['url']}/readme"
    response = requests.get(readme_url)
    
    if response.status_code == 200:
        # GitHub API returns the content in base64 encoding, so we need to decode it
        content = base64.b64decode(response.json()['content']).decode('utf-8')
        repo_name = repo['name']
        
        # Save the README content to a file
        with open(f"{repo_name}_README.md", "w") as file:
            file.write(content)
        print(f"Downloaded README for {repo_name}")
    else:
        print(f"Failed to download README for {repo['name']}")

def main():
    """
    Main function to download README files from all repos in the GitHub organization.
    """
    response = requests.get(API_URL)
    
    if response.status_code == 200:
        repos = response.json()
        for repo in repos:
            download_readme(repo)
    else:
        print("Failed to retrieve repositories")

if __name__ == "__main__":
    main()

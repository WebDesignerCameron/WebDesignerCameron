import re
import requests

# Configuration
USERNAME = "WebDesignerCameron"  # Replace with your target username
FILE_PATH = "README.md"

def get_repo_count(username):
    # Fetch public user details from GitHub REST API
    url = f"https://api.github.com/users/{username}"
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        return data.get("public_repos", 0)
    else:
        raise Exception(f"Failed to fetch data: {response.status_code}")

def update_markdown_file(file_path, count):
    with open(file_path, "r", encoding="utf-8") as file:
        content = file.read()

    # Regex patterns targeting your markdown comment tags
    start_tag = "<!-- REPO_COUNT_START -->"
    end_tag = "<!-- REPO_COUNT_END -->"
    pattern = rf"{start_tag}.*?{end_tag}"
    
    # Replace old content inside markers with the updated count
    replacement = f"{start_tag}\nPublic Repositories: {count}\n{end_tag}"
    new_content = re.sub(pattern, replacement, content, flags=re.DOTALL)

    with open(file_path, "w", encoding="utf-8") as file:
        file.write(new_content)

if __name__ == "__main__":
    try:
        repo_count = get_repo_count(USERNAME)
        update_markdown_file(FILE_PATH, repo_count)
        print(f"Successfully updated repository count to {repo_count}.")
    except Exception as e:
        print(f"Error: {e}")
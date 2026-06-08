import os
from huggingface_hub import HfApi

def deploy():
    env_vars = {}
    with open(".env.txt", "r", encoding="utf-8") as f:
        for line in f:
            if "=" in line:
                key, val = line.strip().split("=", 1)
                env_vars[key] = val

    token = env_vars.get("huggingface_token")
    link = env_vars.get("huggingface_link")
    
    if not token or not link:
        print("Error: Could not find huggingface_token or huggingface_link in .env.txt")
        return

    # Extract repo_id from the link (e.g. https://huggingface.co/spaces/Lee010043/seismology_raspberryPi)
    repo_id = link.split("spaces/")[-1]
    
    print(f"Deploying to repository: {repo_id}")

    api = HfApi(token=token)
    
    api.upload_folder(
        folder_path=".",
        repo_id=repo_id,
        repo_type="space",
        ignore_patterns=[".git*", "__pycache__", "deploy_hf.py", ".env*", "*.docx", "Seismology.txt"]
    )
    print("Deployment successful!")

if __name__ == "__main__":
    deploy()

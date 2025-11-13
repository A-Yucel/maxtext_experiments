#!/usr/bin/env python3
import argparse
from huggingface_hub import HfApi, login

def main():
    parser = argparse.ArgumentParser(description="Upload a folder to a Hugging Face model repo.")
    parser.add_argument("--folder_path", required=True, help="Local folder path to upload.")
    parser.add_argument("--repo_id", required=True, help="Hugging Face repo id (e.g., username/repo_name).")
    args = parser.parse_args()
    print(args)
    api = HfApi()

    # Create repo if it doesn't exist
    api.create_repo(
        repo_id=args.repo_id.strip(),
        repo_type="model",
        private=True,
        exist_ok=True,
    )

    # Upload folder
    print(f"Uploading {args.folder_path} to https://huggingface.co/{args.repo_id} ...")
    api.upload_folder(
        folder_path=args.folder_path.strip(),
        repo_id=args.repo_id.strip(),
        repo_type="model",
    )

    print("✅ Upload complete!")

if __name__ == "__main__":
    main()
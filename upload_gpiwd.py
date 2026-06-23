#!/usr/bin/env python3
"""
Script to upload all GPIWD-Dragon files to GitHub via API.
Handles create and update (upsert) for all files.
"""

import os
import base64
import json
import urllib.request
import urllib.error

GITHUB_TOKEN = os.environ.get("GITHUB_TOKEN", "")
REPO = "Muhamadridwanjr/GPIWD-Dragon"
BASE_DIR = "/root/MR_Automation/github-profile/GPIWD-Dragon"
API_BASE = f"https://api.github.com/repos/{REPO}/contents"

HEADERS = {
    "Authorization": f"token {GITHUB_TOKEN}",
    "Content-Type": "application/json",
    "Accept": "application/vnd.github.v3+json",
}


def api_request(method, url, data=None):
    body = json.dumps(data).encode() if data else None
    req = urllib.request.Request(url, data=body, headers=HEADERS, method=method)
    try:
        with urllib.request.urlopen(req) as resp:
            return json.loads(resp.read()), resp.status
    except urllib.error.HTTPError as e:
        body = json.loads(e.read())
        return body, e.code


def get_file_sha(path):
    """Get SHA of existing file if it exists."""
    url = f"{API_BASE}/{path}"
    data, status = api_request("GET", url)
    if status == 200:
        return data.get("sha")
    return None


def upload_file(local_path, remote_path):
    """Upload a single file to GitHub."""
    with open(local_path, "rb") as f:
        content = base64.b64encode(f.read()).decode()

    sha = get_file_sha(remote_path)

    payload = {
        "message": f"feat: add {remote_path} — GPIWD-Dragon V1.0 build 🐉",
        "content": content,
    }
    if sha:
        payload["sha"] = sha
        payload["message"] = f"feat: update {remote_path} — GPIWD-Dragon V1.0 🔄"

    url = f"{API_BASE}/{remote_path}"
    data, status = api_request("PUT", url, payload)

    if status in (200, 201):
        action = "Updated" if sha else "Created"
        print(f"  ✅ {action}: {remote_path}")
    else:
        print(f"  ❌ Failed ({status}): {remote_path} — {data.get('message', '')}")


def walk_and_upload(base_dir):
    """Walk directory tree and upload all files."""
    files_uploaded = 0
    skip_patterns = [".git", "__pycache__", ".pytest_cache", "node_modules", "venv", ".egg"]

    for root, dirs, files in os.walk(base_dir):
        # Skip hidden/build dirs
        dirs[:] = [d for d in dirs if not any(p in d for p in skip_patterns)]

        for filename in files:
            local_path = os.path.join(root, filename)
            # Calculate relative path
            remote_path = os.path.relpath(local_path, base_dir)

            # Skip binary files and sensitive files
            skip_files = [".env", ".pyc", ".DS_Store"]
            if any(filename.endswith(s) or filename == s for s in skip_files):
                if filename == ".env":  # Allow .env.example but not .env
                    continue
                continue

            print(f"Uploading: {remote_path}")
            upload_file(local_path, remote_path)
            files_uploaded += 1

    return files_uploaded


if __name__ == "__main__":
    print("🐉 GPIWD-Dragon GitHub Upload")
    print(f"📁 Source: {BASE_DIR}")
    print(f"🎯 Target: https://github.com/{REPO}")
    print("=" * 60)

    total = walk_and_upload(BASE_DIR)

    print("=" * 60)
    print(f"✅ Done! Uploaded {total} files.")
    print(f"🌐 View at: https://github.com/{REPO}")

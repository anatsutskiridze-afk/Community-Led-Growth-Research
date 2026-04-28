import requests
import os

API_KEY = "sd_efb5d40e4e8b0306c61bd636754e4fdf"

videos = [
    {"author": "lloyed-lobo", "url": "https://youtu.be/0BxVuTILyyU"},
    {"author": "mac-reddin", "url": "https://youtu.be/cl-w8dN6SWU"},
    {"author": "patrick-woods", "url": "https://youtu.be/KuW6B9757FY"},
    {"author": "jono-bacon", "url": "https://youtu.be/cjzCsQ0iw6o"},
    {"author": "mary-thengvall", "url": "https://youtu.be/UgstKIW8bvg"},
    {"author": "mallory-contois", "url": "https://youtu.be/EBUJVW3p9gc"},
    {"author": "claire-suellentrop", "url": "https://youtu.be/WkHAnvNTHnY"},
    {"author": "adam-duvander", "url": "https://youtu.be/R6Sf34dIImM"},
]

for video in videos:
    response = requests.get(
        "https://api.supadata.ai/v1/youtube/transcript",
        headers={"x-api-key": API_KEY},
        params={"url": video["url"], "text": True}
    )
    
    data = response.json()
    transcript = data.get("content", "No transcript available")
    
    folder = f"research/youtube-transcripts/{video['author']}"
    os.makedirs(folder, exist_ok=True)
    
    with open(f"{folder}/transcript.md", "w") as f:
        f.write(f"# Transcript\n")
        f.write(f"**URL:** {video['url']}\n\n")
        f.write(transcript)
    
    print(f"✓ Saved {video['author']}")

print("Done!")
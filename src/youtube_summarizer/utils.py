import re


def extract_video_id(url):
    """
    Extract YouTube video ID from various URL formats.
    Supports:
    - https://www.youtube.com/watch?v=VIDEO_ID
    - https://youtu.be/VIDEO_ID
    - https://www.youtube.com/embed/VIDEO_ID
    - https://www.youtube.com/v/VIDEO_ID
    - Direct video ID (11 characters)
    """
    patterns = [
        r'(?:youtube\.com\/watch\?v=|youtu\.be\/|youtube\.com\/embed\/|youtube\.com\/v\/)([a-zA-Z0-9_-]{11})',
        r'youtube\.com\/watch\?.*v=([a-zA-Z0-9_-]{11})',
    ]
    
    for pattern in patterns:
        match = re.search(pattern, url)
        if match:
            video_id = match.group(1)
            print(f"✓ Video ID extracted: {video_id}")
            return video_id
    
    if len(url) == 11 and re.match(r'^[a-zA-Z0-9_-]{11}$', url):
        print(f"✓ Direct video ID provided: {url}")
        return url
    
    raise ValueError("Invalid YouTube URL or video ID")

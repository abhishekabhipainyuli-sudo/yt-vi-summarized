import sys
from src.youtube_summarizer import YouTubeVideoSummarizer


def main():
    if len(sys.argv) < 2:
        print("Usage: python main.py <youtube_url_or_video_id>")
        print("\nExamples:")
        print("  python main.py https://www.youtube.com/watch?v=dQw4w9WgXcQ")
        print("  python main.py https://youtu.be/dQw4w9WgXcQ")
        print("  python main.py dQw4w9WgXcQ")
        sys.exit(1)
    
    url = sys.argv[1]
    
    try:
        summarizer = YouTubeVideoSummarizer()
        result = summarizer.process_video(url)
        print("\n✓ Process completed successfully!")
        
    except Exception as e:
        print(f"\n❌ Error: {str(e)}")
        sys.exit(1)


if __name__ == "__main__":
    main()

import os
from pathlib import Path
from dotenv import load_dotenv
from google import genai
import yt_dlp
from .utils import extract_video_id

load_dotenv()


class YouTubeVideoSummarizer:
    def __init__(self, api_key=None):
        self.api_key = api_key or os.getenv('GEMINI_API_KEY')
        if not self.api_key:
            raise ValueError("GEMINI_API_KEY not found in environment variables")
        self.client = genai.Client(api_key=self.api_key)
        self.audio_dir = Path("audio_files")
        self.audio_dir.mkdir(exist_ok=True)
    
    def download_audio(self, video_id):
        """
        Download audio from YouTube video using yt-dlp.
        Returns the path to the downloaded audio file.
        """
        print(f"\n🎵 Downloading audio for video ID: {video_id}...")
        
        output_path = self.audio_dir / f"{video_id}.mp3"
        
        if output_path.exists():
            print(f"✓ Audio file already exists: {output_path}")
            return str(output_path)
        
        ydl_opts = {
            'format': 'bestaudio/best',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }],
            'outtmpl': str(self.audio_dir / f"{video_id}.%(ext)s"),
            'quiet': False,
            'no_warnings': False,
        }
        
        try:
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                url = f"https://www.youtube.com/watch?v={video_id}"
                ydl.download([url])
            
            print(f"✓ Audio downloaded successfully: {output_path}")
            return str(output_path)
        
        except Exception as e:
            raise Exception(f"Failed to download audio: {str(e)}")
    
    def transcribe_audio(self, audio_path):
        """
        Transcribe audio file to text using Google Gemini API.
        """
        print(f"\n📝 Transcribing audio to text with Gemini...")
        
        uploaded_file = None
        try:
            print("   Uploading audio file...")
            uploaded_file = self.client.files.upload(file=audio_path)
            
            print("   Processing transcription...")
            response = self.client.models.generate_content(
                model="gemini-2.5-flash",
                contents=[
                    uploaded_file,
                    "Please transcribe this audio file. Provide only the transcribed text without any additional commentary."
                ]
            )
            
            transcript = response.text if response.text else ""
            
            if not transcript:
                raise ValueError("Gemini returned an empty transcription")
            
            print(f"✓ Transcription completed successfully!")
            print(f"   Transcript length: {len(transcript)} characters")
            
            return transcript
        
        except Exception as e:
            raise Exception(f"Failed to transcribe audio: {str(e)}")
        
        finally:
            if uploaded_file and uploaded_file.name:
                try:
                    self.client.files.delete(name=uploaded_file.name)
                except Exception:
                    pass
    
    def process_video(self, url):
        """
        Complete pipeline: Extract video ID -> Download audio -> Transcribe to text.
        """
        print("=" * 60)
        print("YouTube Video to Text Converter")
        print("=" * 60)
        
        video_id = extract_video_id(url)
        
        audio_path = self.download_audio(video_id)
        
        transcript = self.transcribe_audio(audio_path)
        
        print("\n" + "=" * 60)
        print("TRANSCRIPTION RESULT")
        print("=" * 60)
        print(transcript)
        print("=" * 60)
        
        return {
            'video_id': video_id,
            'audio_path': audio_path,
            'transcript': transcript
        }

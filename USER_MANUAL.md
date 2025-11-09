# YouTube Video Transcriber - User Manual

## 🎯 Overview

The YouTube Video Transcriber is a powerful web application that converts YouTube videos to text using AI-powered transcription. Simply paste a YouTube URL and get an accurate transcript in seconds!

---

## 🚀 Getting Started

### Prerequisites

Before you begin, you'll need:
- A Google Gemini API key (free to obtain)
- Internet connection
- A YouTube video URL

### Setting Up Your API Key

1. **Get Your Free API Key:**
   - Visit: https://aistudio.google.com/apikey
   - Sign in with your Google account
   - Click "Create API Key"
   - Copy the key to your clipboard

2. **Add to Replit Secrets:**
   - Click the "Secrets" tab in Replit (lock icon on the left sidebar)
   - Click "New Secret"
   - Key: `GEMINI_API_KEY`
   - Value: Paste your API key
   - Click "Save"

3. **Restart the Application:**
   - The app will automatically detect the new key
   - You're ready to transcribe videos!

---

## 💡 How to Use the Web Interface

### Step-by-Step Guide

1. **Access the App:**
   - The web interface should automatically open when you run the project
   - Look for the "Webview" tab in Replit

2. **Enter a YouTube Video:**
   - Find the text input box labeled "YouTube URL or Video ID"
   - Paste any of these formats:
     - Full URL: `https://www.youtube.com/watch?v=dQw4w9WgXcQ`
     - Short URL: `https://youtu.be/dQw4w9WgXcQ`
     - Video ID only: `dQw4w9WgXcQ`

3. **Transcribe:**
   - Click the "🎙️ Transcribe Video" button
   - Wait while the app:
     - Downloads the audio from YouTube
     - Sends it to Google Gemini AI
     - Transcribes the audio to text

4. **View Results:**
   - The transcript will appear in a text box
   - You'll see:
     - Character count
     - Full transcript text
     - Video preview

5. **Save Your Transcript:**
   - Click "💾 Download as TXT" to save to your computer
   - Or copy the text directly from the text area

---

## 🎬 Example Videos to Try

Here are some video IDs you can use to test:

- `dQw4w9WgXcQ` - Popular music video
- `jNQXAC9IVRw` - "Me at the zoo" (first YouTube video ever)

**Pro Tip:** Start with shorter videos (under 5 minutes) for faster processing!

---

## 📱 Using the Command Line Interface (CLI)

If you prefer the command line, you can also use the app this way:

```bash
python main.py <youtube_url_or_video_id>
```

### Examples:

```bash
# Using full URL
python main.py https://www.youtube.com/watch?v=dQw4w9WgXcQ

# Using short URL
python main.py https://youtu.be/dQw4w9WgXcQ

# Using just the video ID
python main.py dQw4w9WgXcQ
```

The transcript will be displayed in the console.

---

## ⚙️ Features

### Current Features

✅ **Extract Video ID** - Automatically detects video ID from various URL formats  
✅ **Download Audio** - Extracts high-quality audio from YouTube videos  
✅ **AI Transcription** - Uses Google Gemini AI for accurate transcription  
✅ **Web Interface** - Easy-to-use web application  
✅ **Download Transcripts** - Save transcripts as text files  
✅ **Video Preview** - See the video you're transcribing  
✅ **Progress Indicators** - Visual feedback during processing  
✅ **Audio Caching** - Reuses downloaded audio for same videos  

### Coming Soon

🔄 **Text Summarization** - Get concise summaries of transcripts  
📊 **Batch Processing** - Transcribe multiple videos at once  
📝 **Multiple Formats** - Export to JSON, PDF, and more  
🎨 **Custom Styling** - Choose summary length and style  

---

## 🔧 Technical Details

### How It Works

1. **Video ID Extraction**
   - Parses the YouTube URL
   - Extracts the unique 11-character video ID

2. **Audio Download**
   - Uses yt-dlp to download video
   - Converts to MP3 format using FFmpeg
   - Saves to `audio_files/` directory

3. **AI Transcription**
   - Uploads audio to Google Gemini
   - Gemini's multimodal AI transcribes the audio
   - Returns accurate text transcript

4. **Display & Export**
   - Shows results in web interface
   - Allows download as text file

### Technologies Used

- **Python 3.11+** - Programming language
- **Streamlit** - Web interface framework
- **yt-dlp** - YouTube video/audio downloader
- **Google Gemini AI** - Audio transcription engine
- **FFmpeg** - Audio format conversion
- **python-dotenv** - Environment variable management

### File Structure

```
youtube-video-summarizer/
├── app.py                      # Streamlit web interface
├── main.py                     # CLI entry point
├── src/
│   └── youtube_summarizer/
│       ├── __init__.py
│       ├── summarizer.py       # Core transcription logic
│       └── utils.py            # Helper functions
├── audio_files/                # Downloaded audio cache
├── requirements.txt            # Python dependencies
├── pyproject.toml             # Project configuration
├── USER_MANUAL.md             # This file
└── README.md                  # Project overview
```

---

## ❓ Troubleshooting

### "GEMINI_API_KEY not found"

**Problem:** The app can't find your API key.

**Solution:**
1. Check that you added the key to Replit Secrets
2. Make sure it's named exactly `GEMINI_API_KEY`
3. Restart the application

### "Invalid URL"

**Problem:** The app doesn't recognize your YouTube URL.

**Solution:**
1. Make sure you're using a valid YouTube URL
2. Try using just the video ID instead
3. Check that the URL is complete and correct

### "Download Failed"

**Problem:** The app can't download the video.

**Solution:**
1. Check your internet connection
2. Make sure the video is public (not private)
3. Try a different video
4. Some videos may be restricted by region or copyright

### Video Takes Too Long

**Problem:** Processing seems stuck.

**Solution:**
1. Longer videos take more time (up to several minutes)
2. Check the progress spinners to see what's happening
3. Try a shorter video first to verify everything works
4. Refresh the page if stuck for more than 5 minutes

---

## 🔒 Privacy & Security

- **API Keys:** Your Gemini API key is stored securely in Replit Secrets
- **Audio Files:** Downloaded audio is cached locally for reuse
- **Data:** Transcripts are processed through Google's Gemini API
- **No Storage:** We don't store your videos or transcripts on our servers

---

## 💰 Cost Information

- **Google Gemini API:** Free tier includes generous usage limits
- **YouTube Access:** Free
- **This App:** Completely free to use

**Note:** If you transcribe many long videos, you may hit Gemini's free tier limits. Check Google's pricing for details.

---

## 📞 Support

### Common Questions

**Q: What video formats are supported?**  
A: Any YouTube video that can be accessed via URL.

**Q: How long can the video be?**  
A: No strict limit, but longer videos take more time to process.

**Q: Can I transcribe private videos?**  
A: No, only public or unlisted videos that are accessible via URL.

**Q: Is the transcription accurate?**  
A: Google Gemini provides high accuracy, especially for clear audio.

**Q: Can I transcribe videos in other languages?**  
A: Yes! Gemini supports multiple languages automatically.

---

## 📝 Tips for Best Results

1. **Clear Audio:** Videos with clear speech transcribe better
2. **Language:** Single-language videos work best
3. **Background Noise:** Minimal background noise improves accuracy
4. **Video Length:** Start with shorter videos to test
5. **Internet Speed:** Faster internet = faster processing

---

## 🎓 Learning Resources

### Want to Learn More?

- **YouTube API:** https://developers.google.com/youtube
- **Google Gemini:** https://ai.google.dev/
- **yt-dlp Documentation:** https://github.com/yt-dlp/yt-dlp
- **Streamlit Docs:** https://docs.streamlit.io/

---

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

---

**Last Updated:** November 9, 2025  
**Version:** 1.0.0

# YouTube Video Transcriber

## Overview

This is a Python-based application with a beautiful Streamlit web interface that processes YouTube videos by extracting audio and transcribing it to text using Google Gemini's multimodal API. The application handles various YouTube URL formats, downloads audio content, and converts it to text transcription. Both web interface and command-line interface are available. A text summarization feature is planned for future implementation.

**Latest Update (November 2025):**
- ✅ Added Streamlit web interface for easy video transcription
- ✅ Created comprehensive USER_MANUAL.md documentation
- ✅ Updated README with web interface instructions
- ✅ Configured workflow to run web UI on port 5000

## User Preferences

Preferred communication style: Simple, everyday language.

## System Architecture

### Application Structure

**Modular Package Design**
- The application uses a structured package architecture organized in `src/youtube_summarizer/`
- Main components:
  - `summarizer.py`: Core `YouTubeVideoSummarizer` class
  - `utils.py`: Helper functions (video ID extraction)
  - `__init__.py`: Package initialization and exports
- Entry points:
  - `app.py`: Streamlit web interface (primary)
  - `main.py`: Command-line interface
- Rationale: Organized structure allows for easy testing, maintenance, and future expansion

### Core Components

**1. YouTube Video Processing**
- Uses `yt-dlp` library as the video download engine
- Supports multiple URL formats through regex pattern matching:
  - Standard YouTube URLs (`youtube.com/watch?v=`)
  - Short URLs (`youtu.be/`)
  - Embed URLs (`youtube.com/embed/`)
  - Direct video IDs (11-character alphanumeric strings)
- Audio files are stored in a dedicated `audio_files/` directory to keep the workspace organized

**2. Audio Transcription**
- Integrates with Google Gemini API for speech-to-text conversion using multimodal AI capabilities
- Uses the official Google GenAI Python client library for API communication
- Requires valid Gemini API key for operation

**3. Configuration Management**
- Uses environment variables for sensitive configuration (API keys)
- Implements `python-dotenv` for local development environment setup
- Pattern: Separates configuration from code for security and flexibility

### Data Flow

**Web Interface Flow (Primary):**
1. User accesses Streamlit web interface
2. User pastes YouTube URL or video ID into input field
3. Application validates and extracts video ID using regex patterns
4. Progress indicators show download and transcription status
5. Audio is downloaded from YouTube and cached in `audio_files/`
6. Audio file is uploaded to Google Gemini API
7. Gemini processes the audio and returns transcription
8. Transcript is displayed in the UI with download option
9. Video preview is shown alongside transcript
10. Uploaded file is cleaned up from Gemini storage

**CLI Flow (Alternative):**
1. User provides YouTube URL or video ID via command-line argument
2. Application extracts/validates the video ID
3. Audio is downloaded and transcribed
4. Transcription text is displayed in the console

### Security Architecture

**API Key Management**
- Gemini API key stored in `.env` file (excluded from version control via `.env.example` pattern)
- Key validation occurs at initialization to fail fast if misconfigured
- Rationale: Prevents accidental exposure of credentials while maintaining ease of local development

### File System Design

**Local Storage Strategy**
- Creates `audio_files/` directory for temporary audio storage
- Uses Python's `pathlib.Path` for cross-platform file path handling
- Directory created automatically if it doesn't exist

## External Dependencies

### Third-Party Services

**Google Gemini API**
- Purpose: Audio-to-text transcription service using multimodal AI
- Authentication: API key-based
- Integration point: Google GenAI Python client library
- Required setup: API key from https://aistudio.google.com/apikey

### Python Libraries

**yt-dlp**
- Purpose: YouTube video/audio downloading
- Why chosen: Industry-standard tool for YouTube content extraction, actively maintained fork of youtube-dl
- Alternative considered: youtube-dl (less actively maintained)

**google-genai**
- Purpose: Official client for Google Gemini API services
- Provides: Multimodal AI capabilities including audio transcription

**streamlit**
- Purpose: Web interface framework for the application
- Why chosen: Easy-to-use, Python-native, perfect for data applications
- Provides: Interactive UI components, file downloads, progress indicators
- Configured: Runs on port 5000 with 0.0.0.0 binding for Replit compatibility

**python-dotenv**
- Purpose: Environment variable management for local development
- Pattern: Enables .env file loading for configuration

**ffmpeg**
- Purpose: Audio format conversion and processing
- Role: Used by yt-dlp for audio extraction from video containers
- Note: System-level dependency, not a Python package

### Future Dependencies

Text summarization feature (planned) will likely require:
- Additional Gemini API calls (using the same multimodal model for summarization)
- Potential need for text chunking if transcriptions exceed token limits
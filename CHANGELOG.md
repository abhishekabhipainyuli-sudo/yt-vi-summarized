# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.0.0] - 2025-11-09

### Added
- Initial release
- YouTube video ID extraction from multiple URL formats
- Audio download and extraction using yt-dlp
- Audio-to-text transcription using Google Gemini API
- Automatic cleanup of uploaded files
- Command-line interface
- Structured codebase with src/ directory organization
- Comprehensive documentation
- Environment variable configuration
- Error handling and validation

### Features
- Support for standard YouTube URLs (youtube.com/watch?v=)
- Support for short URLs (youtu.be/)
- Support for embed URLs (youtube.com/embed/)
- Support for direct video IDs
- MP3 audio format with 192kbps quality
- Cached audio files to avoid re-downloading
- Progress indicators for download and transcription
- Clean console output with status messages

### Technical
- Python 3.11+ support
- Google Gemini 2.5 Flash model integration
- Modular architecture with separate utilities
- Comprehensive .gitignore
- MIT License
- Project metadata in app.json
- Requirements file for dependency management

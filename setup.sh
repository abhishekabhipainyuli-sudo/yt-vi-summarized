#!/bin/bash

echo "=========================================="
echo "YouTube Video Summarizer Setup"
echo "=========================================="
echo ""

# Check Python version
echo "Checking Python version..."
python_version=$(python --version 2>&1 | awk '{print $2}')
echo "Python version: $python_version"
echo ""

# Install dependencies
echo "Installing dependencies..."
if command -v uv &> /dev/null; then
    echo "Using uv for faster installation..."
    uv sync
else
    echo "Using pip..."
    pip install -r requirements.txt
fi
echo ""

# Check for .env file
if [ ! -f .env ]; then
    echo "Creating .env file from template..."
    cp app.env .env
    echo "✓ .env file created"
    echo ""
    echo "⚠️  IMPORTANT: Please edit .env and add your GEMINI_API_KEY"
    echo "   Get your API key from: https://aistudio.google.com/apikey"
else
    echo "✓ .env file already exists"
fi
echo ""

# Create audio_files directory
echo "Creating audio_files directory..."
mkdir -p audio_files
echo "✓ audio_files directory created"
echo ""

echo "=========================================="
echo "Setup Complete!"
echo "=========================================="
echo ""
echo "Next steps:"
echo "1. Edit .env and add your GEMINI_API_KEY"
echo "2. Run: python main.py <youtube_url>"
echo ""
echo "Example:"
echo "  python main.py https://www.youtube.com/watch?v=dQw4w9WgXcQ"
echo ""

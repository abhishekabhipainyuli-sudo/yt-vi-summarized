# Contributing to YouTube Video Summarizer

Thank you for your interest in contributing to this project!

## Getting Started

1. Fork the repository
2. Clone your fork: `git clone https://github.com/yourusername/youtube-video-summarizer.git`
3. Create a branch: `git checkout -b feature/your-feature-name`
4. Make your changes
5. Test your changes
6. Commit: `git commit -m "Add your feature"`
7. Push: `git push origin feature/your-feature-name`
8. Create a Pull Request

## Development Setup

```bash
# Install dependencies
pip install -r requirements.txt

# Or using uv
uv sync

# Set up environment
cp app.env .env
# Add your GEMINI_API_KEY to .env
```

## Code Style

- Follow PEP 8 guidelines
- Use meaningful variable and function names
- Add docstrings to functions and classes
- Keep functions focused and small
- Add comments for complex logic

## Testing

Before submitting a PR:
- Test with different YouTube URL formats
- Verify error handling works correctly
- Check that audio files are cleaned up properly
- Ensure console output is clear and helpful

## Pull Request Guidelines

- Describe what your PR does
- Link to any related issues
- Include examples of usage if adding new features
- Update documentation if needed
- Keep PRs focused on a single feature or fix

## Reporting Issues

When reporting issues, please include:
- Description of the problem
- Steps to reproduce
- Expected behavior
- Actual behavior
- Python version
- Operating system

## Feature Requests

We welcome feature requests! Please:
- Check if the feature was already requested
- Describe the use case
- Explain why it would be useful
- Provide examples if possible

## Code of Conduct

- Be respectful and inclusive
- Provide constructive feedback
- Focus on the issue, not the person
- Help others learn and grow

Thank you for contributing!

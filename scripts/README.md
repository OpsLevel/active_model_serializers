# Python Scripts

This directory contains Python scripts and tooling for the ActiveModelSerializers project.

## Requirements

- Python 3.11 or later (latest version recommended)
- See `requirements.txt` in the root directory for dependencies

## Available Scripts

### test.py

Tests Python compatibility and ensures the environment is properly configured with the latest Python features.

Usage:
```bash
python scripts/test.py
```

## Development

To set up the Python development environment:

```bash
# Install Python 3.11+ (if not already installed)
# On Ubuntu/Debian:
sudo apt-get update
sudo apt-get install python3.11

# On macOS with Homebrew:
brew install python@3.11

# Install dependencies
pip install -r requirements.txt

# For development tools (optional)
pip install -e ".[dev]"
```

## CI/CD

Python tests are automatically run via GitHub Actions on every push and pull request. See `.github/workflows/python.yml` for details.

# Python Quick Start Guide

## Prerequisites
- Python 3.11 or later (3.12 recommended)

## Quick Commands

### Check Python Version
```bash
python3 --version
```
Expected output: `Python 3.11.x` or higher

### First-Time Setup
```bash
python3 scripts/setup.py
```

### Run Tests
```bash
python3 scripts/test.py
```

## Installation

### Ubuntu/Debian
```bash
sudo apt-get update
sudo apt-get install python3.11
```

### macOS (Homebrew)
```bash
brew install python@3.11
```

### Verify Installation
```bash
python3 --version  # Should show 3.11 or higher
python3 scripts/test.py  # All tests should pass
```

## Troubleshooting

### "Python version not supported"
- **Problem**: Python version is older than 3.11
- **Solution**: Install Python 3.11 or later

### Script won't execute
- **Problem**: Permission denied
- **Solution**: 
  ```bash
  chmod +x scripts/*.py
  # or run with python3:
  python3 scripts/test.py
  ```

### Import errors
- **Problem**: Missing dependencies
- **Solution**: 
  ```bash
  python3 scripts/setup.py
  ```

## CI/CD

GitHub Actions automatically tests every push with:
- Python 3.11
- Python 3.12

See `.github/workflows/python.yml` for details.

## Documentation

- **Scripts**: See [scripts/README.md](scripts/README.md)
- **Project Config**: See [pyproject.toml](pyproject.toml)
- **Main README**: See [README.md](README.md)

## Getting Help

If you encounter issues:
1. Check that Python 3.11+ is installed: `python3 --version`
2. Run the setup script: `python3 scripts/setup.py`
3. Check the full documentation in `scripts/README.md`
4. Review error messages - they include helpful hints

## Success Indicators

When everything is working, you'll see:
```
==================================================
All tests passed! ✓
==================================================
```

No errors means you're good to go! 🎉

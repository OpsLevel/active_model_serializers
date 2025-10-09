#!/usr/bin/env python3
"""
Setup script to verify Python environment and dependencies.
"""
import sys
import subprocess
from pathlib import Path


def check_python_version():
    """Check if Python version is 3.11 or later."""
    version = sys.version_info
    print(f"Current Python version: {version.major}.{version.minor}.{version.micro}")
    
    if version < (3, 11):
        print("❌ Error: Python 3.11 or later is required")
        print("   Please upgrade your Python installation")
        return False
    
    print("✓ Python version is compatible")
    return True


def install_dependencies():
    """Install required dependencies."""
    print("\nInstalling dependencies...")
    requirements_file = Path(__file__).parent.parent / "requirements.txt"
    
    if requirements_file.exists():
        try:
            subprocess.check_call([
                sys.executable, "-m", "pip", "install", "-r", str(requirements_file)
            ])
            print("✓ Dependencies installed")
            return True
        except subprocess.CalledProcessError:
            print("❌ Failed to install dependencies")
            return False
    else:
        print("⚠ No requirements.txt found, skipping dependency installation")
        return True


def run_tests():
    """Run the test script to verify setup."""
    print("\nRunning tests...")
    test_script = Path(__file__).parent / "test.py"
    
    try:
        result = subprocess.run([sys.executable, str(test_script)], check=True)
        return result.returncode == 0
    except subprocess.CalledProcessError:
        print("❌ Tests failed")
        return False


def main():
    """Run the setup process."""
    print("=" * 50)
    print("Python Environment Setup")
    print("=" * 50)
    
    if not check_python_version():
        return 1
    
    if not install_dependencies():
        return 1
    
    if not run_tests():
        return 1
    
    print("\n" + "=" * 50)
    print("Setup completed successfully! ✓")
    print("=" * 50)
    return 0


if __name__ == "__main__":
    sys.exit(main())

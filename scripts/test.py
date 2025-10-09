#!/usr/bin/env python3
"""
Test script to verify Python compatibility with the latest Python versions.
This script uses modern Python features to ensure compatibility.
"""
import sys
import platform


def test_python_version():
    """Test that we're running on a supported Python version."""
    version_info = sys.version_info
    print(f"Python version: {platform.python_version()}")
    print(f"Python implementation: {platform.python_implementation()}")
    
    if version_info < (3, 11):
        raise RuntimeError(
            f"Python version {version_info.major}.{version_info.minor} is not supported. "
            "Please use Python 3.11 or later."
        )
    print("✓ Python version check passed")


def test_modern_features():
    """Test modern Python features to ensure compatibility."""
    # Test f-strings with = (Python 3.8+)
    value = 42
    debug_str = f"{value=}"
    assert "value=42" in debug_str
    print("✓ Modern f-string features work")
    
    # Test match statement (Python 3.10+)
    def test_match(value):
        match value:
            case 1:
                return "one"
            case 2:
                return "two"
            case _:
                return "other"
    
    assert test_match(1) == "one"
    print("✓ Match statement works")
    
    # Test type hints with | (Python 3.10+)
    def test_union(value: str | int) -> str:
        return str(value)
    
    assert test_union(42) == "42"
    assert test_union("hello") == "hello"
    print("✓ Modern type hints work")


def main():
    """Run all tests."""
    print("=" * 50)
    print("Testing Python compatibility")
    print("=" * 50)
    
    try:
        test_python_version()
        test_modern_features()
        print("\n" + "=" * 50)
        print("All tests passed! ✓")
        print("=" * 50)
        return 0
    except Exception as e:
        print(f"\n❌ Test failed: {e}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    sys.exit(main())

#!/usr/bin/env python3
"""
README Scanner Tool

This script scans repositories to identify those without a README file
and validates that existing READMEs meet organizational documentation standards.

Usage:
    python scripts/scan_readme.py [repository_path]

If no repository path is provided, it scans the current directory.
"""

import os
import sys
import re
from typing import Dict, List, Tuple


class READMEScanner:
    """Scanner to check README presence and compliance with standards."""

    REQUIRED_SECTIONS = [
        'title',
        'description',
        'installation',
        'usage',
        'contributing',
        'license'
    ]

    def __init__(self, repo_path: str = '.'):
        self.repo_path = os.path.abspath(repo_path)
        self.repo_name = os.path.basename(self.repo_path)

    def scan(self) -> Dict:
        """
        Scan the repository for README and check compliance.

        Returns:
            Dictionary with scan results including:
            - exists: bool
            - path: str or None
            - sections: dict of section presence
            - compliant: bool
            - issues: list of issues found
        """
        result = {
            'repository': self.repo_name,
            'path': self.repo_path,
            'exists': False,
            'readme_path': None,
            'sections': {},
            'compliant': False,
            'issues': []
        }

        # Check for README existence
        readme_path = self._find_readme()

        if not readme_path:
            result['issues'].append('README.md not found in repository root')
            return result

        result['exists'] = True
        result['readme_path'] = readme_path

        # Check sections
        sections = self._check_sections(readme_path)
        result['sections'] = sections

        # Identify missing sections
        missing_sections = [
            section for section, present in sections.items()
            if not present
        ]

        if missing_sections:
            for section in missing_sections:
                result['issues'].append(f'Missing {section} section')

        # Check compliance
        result['compliant'] = len(missing_sections) == 0

        return result

    def _find_readme(self) -> str or None:
        """Find README.md in the repository root."""
        readme_names = ['README.md', 'README.MD', 'readme.md', 'Readme.md']

        for name in readme_names:
            path = os.path.join(self.repo_path, name)
            if os.path.exists(path):
                return path

        return None

    def _check_sections(self, readme_path: str) -> Dict[str, bool]:
        """
        Check if README contains required sections.

        Returns:
            Dictionary mapping section names to presence (bool)
        """
        sections = {section: False for section in self.REQUIRED_SECTIONS}

        try:
            with open(readme_path, 'r', encoding='utf-8') as f:
                content = f.read()
                content_lower = content.lower()
        except Exception as e:
            print(f"Error reading README: {e}")
            return sections

        # Check for title (should have # at the beginning)
        if re.search(r'^#\s+\w+', content, re.MULTILINE):
            sections['title'] = True

        # Check for description/about
        if 'about' in content_lower or 'description' in content_lower:
            sections['description'] = True

        # Check for installation
        if 'install' in content_lower or 'setup' in content_lower or 'getting started' in content_lower:
            sections['installation'] = True

        # Check for usage
        if 'usage' in content_lower or 'how to' in content_lower or 'documentation' in content_lower:
            sections['usage'] = True

        # Check for contributing
        if 'contribut' in content_lower:
            sections['contributing'] = True

        # Check for license
        if 'license' in content_lower or 'licensing' in content_lower:
            sections['license'] = True

        return sections

    def print_report(self, result: Dict):
        """Print a formatted report of the scan results."""
        print("=" * 70)
        print(f"README Scan Report: {result['repository']}")
        print("=" * 70)
        print()

        # README existence
        if result['exists']:
            print(f"✅ README found: {os.path.basename(result['readme_path'])}")
        else:
            print("❌ README NOT FOUND")
            print()
            print("Action Required:")
            print("  Create README.md in the repository root with the following sections:")
            print("  - Title")
            print("  - Description")
            print("  - Installation")
            print("  - Usage")
            print("  - Contributing")
            print("  - License")
            return

        print()

        # Section analysis
        print("Section Analysis:")
        print("-" * 70)

        for section, present in result['sections'].items():
            status = "✅" if present else "❌"
            print(f"{status} {section.capitalize()}: {'Present' if present else 'Missing'}")

        print()

        # Compliance status
        if result['compliant']:
            print("=" * 70)
            print("✅ README COMPLIANT with organizational standards")
            print("=" * 70)
        else:
            print("=" * 70)
            print("⚠️  README needs updates to meet standards")
            print("=" * 70)
            print()
            print("Issues found:")
            for i, issue in enumerate(result['issues'], 1):
                print(f"  {i}. {issue}")

        print()


def main():
    """Main entry point for the README scanner."""
    # Determine repository path
    if len(sys.argv) > 1:
        repo_path = sys.argv[1]
    else:
        repo_path = '.'

    # Validate path
    if not os.path.isdir(repo_path):
        print(f"Error: '{repo_path}' is not a valid directory")
        sys.exit(1)

    # Scan repository
    scanner = READMEScanner(repo_path)
    result = scanner.scan()

    # Print report
    scanner.print_report(result)

    # Exit with appropriate code
    sys.exit(0 if result['compliant'] else 1)


if __name__ == '__main__':
    main()

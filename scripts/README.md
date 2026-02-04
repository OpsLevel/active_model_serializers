# Scripts Directory

This directory contains tools and templates for maintaining README documentation standards across the organization.

## Files

### scan_readme.py

A Python script to scan repositories and validate README compliance with organizational standards.

**Usage:**
```bash
# Scan current repository
python scripts/scan_readme.py

# Scan specific repository
python scripts/scan_readme.py /path/to/repository
```

**Features:**
- Checks for README.md existence in repository root
- Validates presence of required sections (title, description, installation, usage, contributing, license)
- Generates compliance report
- Returns exit code 0 for compliant READMEs, 1 otherwise

### README_TEMPLATE.md

A standardized template for creating new README files. Copy this template when starting a new repository or updating an existing README to meet organizational standards.

**Sections included:**
- Title
- About/Description
- Installation
- Usage
- Documentation
- Getting Help
- Contributing
- License
- Optional sections (Requirements, Configuration, Testing, Deployment, etc.)

### README_STANDARDS.md

Comprehensive documentation of organizational README standards and best practices.

**Contents:**
- Required sections
- Recommended optional sections
- Formatting guidelines
- Examples
- Validation tools
- Best practices
- Enforcement guidelines

## Quick Start

To ensure your repository's README meets organizational standards:

1. **Check compliance:**
   ```bash
   python scripts/scan_readme.py
   ```

2. **If starting a new README:**
   - Copy `README_TEMPLATE.md` to your repository root as `README.md`
   - Fill in project-specific details
   - Run scanner to verify

3. **If updating existing README:**
   - Review `README_STANDARDS.md` for requirements
   - Add any missing sections
   - Run scanner to verify compliance

## Requirements

- Python 3.6 or higher
- No external dependencies (uses standard library only)

## Support

For questions or issues with README standards:
- Review [README_STANDARDS.md](README_STANDARDS.md)
- Check the template
- Run the scanner tool for automated validation

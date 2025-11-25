# Changie - Automated Changelog

This directory contains the Changie configuration for automated changelog generation.

## What is Changie?

[Changie](https://changie.dev/) is an automated changelog tool that helps maintain a clean, organized changelog. Instead of manually editing the CHANGELOG.md file, contributors create individual change files that are later merged into the changelog during releases.

## How to Use

### Installing Changie

Install Changie using one of these methods:

```bash
# Using Homebrew (macOS/Linux)
brew tap miniscruff/changie https://github.com/miniscruff/changie
brew install changie

# Using Go
go install github.com/miniscruff/changie@latest

# Or download from https://github.com/miniscruff/changie/releases
```

### Creating a Change Entry

When making a contribution, create a change entry:

```bash
changie new
```

You'll be prompted to:
1. Select a change kind (breaking, feature, fix, misc)
2. Enter a description of your change

This creates a new file in `.changes/unreleased/` with your change description.

### Change Kinds

- **breaking**: Breaking changes that require users to modify their code
- **feature**: New features or enhancements
- **fix**: Bug fixes
- **misc**: Miscellaneous changes (documentation, refactoring, etc.)

### Example

```bash
$ changie new
✔ Kind: feature
✔ Body: Add support for custom serializers
```

This creates a file like `.changes/unreleased/feature_20231125_123456.yaml` containing your change.

## For Maintainers

### Generating a Release

When creating a new release, use:

```bash
# Create version entries from unreleased changes
changie batch <version>

# Merge batched changes into CHANGELOG.md
changie merge
```

## More Information

- [Changie Documentation](https://changie.dev/)
- [Changie GitHub](https://github.com/miniscruff/changie)

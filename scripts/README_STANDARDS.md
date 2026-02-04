# README Documentation Standards

This document outlines the organizational standards for README files in all repositories.

## Overview

Every repository must have a `README.md` file in the root directory that serves as the primary entry point for understanding the project. The README should be clear, comprehensive, and follow the standard structure outlined below.

## Required Sections

All README files must include the following sections:

### 1. Title

- Should be a level 1 heading (`#`) at the top of the file
- Should clearly state the project name
- Example: `# ActiveModelSerializers`

### 2. Description/About

- A brief overview of what the project does
- Key features and purpose
- Current status (if relevant)
- Section heading: `## About` or `## Description`

### 3. Installation

- Clear instructions on how to install or set up the project
- For Ruby gems, include Gemfile instructions
- Include both bundler and gem install methods
- Platform-specific instructions if applicable
- Section heading: `## Installation`

Example for Ruby gems:
```markdown
## Installation

Add this line to your application's Gemfile:

\`\`\`ruby
gem 'project-name'
\`\`\`

And then execute:

\`\`\`bash
$ bundle install
\`\`\`
```

### 4. Usage

- Basic usage examples
- Code snippets demonstrating common use cases
- Links to detailed documentation
- Section heading: `## Usage` or `## Documentation`

### 5. Contributing

- How to contribute to the project
- Link to CONTRIBUTING.md if available
- Pull request guidelines
- Section heading: `## Contributing`

### 6. License

- License type (MIT, Apache, etc.)
- Link to LICENSE file
- Section heading: `## License`

Example:
```markdown
## License

This project is licensed under the MIT License - see the [MIT-LICENSE](MIT-LICENSE) file for details
```

## Recommended Optional Sections

Consider including these sections when relevant:

- **Getting Help**: Where to ask questions (Stack Overflow, Slack, etc.)
- **Requirements**: System requirements, dependencies
- **Configuration**: Setup and configuration instructions
- **Running Tests**: How to run the test suite
- **Changelog**: Link to CHANGELOG.md
- **Code of Conduct**: Link to CODE_OF_CONDUCT.md
- **Versioning**: Semantic versioning statement
- **Alternatives**: Similar projects or alternatives
- **Acknowledgments**: Credits, inspiration, related projects

## Formatting Guidelines

1. **Use Markdown**: All README files should be in Markdown format (`.md`)
2. **Clear Headings**: Use proper heading hierarchy (H1 for title, H2 for main sections)
3. **Code Blocks**: Use fenced code blocks with language identifiers
4. **Links**: Use descriptive link text, not raw URLs
5. **Lists**: Use bullet points or numbered lists for clarity
6. **Emphasis**: Use bold and italic sparingly for emphasis
7. **Line Length**: Keep lines to a reasonable length for readability
8. **Blank Lines**: Use blank lines to separate sections

## Examples

See these repositories for well-formatted READMEs:
- [Active Model Serializers](../README.md)
- [Template](README_TEMPLATE.md)

## Validation

Use the provided scanner tool to validate README compliance:

```bash
python scripts/scan_readme.py
```

This will check for:
- README existence
- Required sections presence
- Overall compliance with standards

## Tools

### README Scanner

Location: `scripts/scan_readme.py`

Usage:
```bash
# Scan current repository
python scripts/scan_readme.py

# Scan specific repository
python scripts/scan_readme.py /path/to/repository
```

### README Template

Location: `scripts/README_TEMPLATE.md`

Copy this template to start a new README with all required sections.

## Best Practices

1. **Keep it Updated**: Regularly review and update the README
2. **Be Concise**: Provide essential information without overwhelming detail
3. **Link to Details**: Use links to reference detailed documentation
4. **Show Examples**: Include practical code examples
5. **Test Instructions**: Verify that setup instructions work
6. **Consider Audience**: Write for both beginners and experienced users
7. **Use Screenshots**: Add visual elements when helpful (optional)
8. **Maintain Consistency**: Follow organizational style guide

## Enforcement

- All new repositories must have a compliant README before merging
- Existing repositories should be audited and updated
- Pull requests updating project setup should also update README
- Use automated checks in CI/CD pipelines where possible

## Questions or Issues

If you have questions about README standards or need help creating one:
1. Check this documentation
2. Review the template
3. Run the scanner tool
4. Consult with the documentation team

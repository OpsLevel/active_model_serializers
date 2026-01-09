# Threat Model Template

This template provides a standardized structure for creating and maintaining threat models across features, services, or projects.

---

## Document Information

- **System/Feature Name**: [Name of the system or feature being analyzed]
- **Version**: [Version number, e.g., 1.0]
- **Last Updated**: [YYYY-MM-DD]
- **Document Owner**: [Team or individual responsible]
- **Review Cycle**: [e.g., Quarterly, Bi-annually]
- **Status**: [Draft, Active, Archived]

---

## Table of Contents

1. [Executive Summary](#executive-summary)
2. [System Architecture Overview](#system-architecture-overview)
3. [Assets and Data Classification](#assets-and-data-classification)
4. [Trust Boundaries](#trust-boundaries)
5. [Threat Analysis (STRIDE)](#threat-analysis-stride)
6. [Attack Vectors and Entry Points](#attack-vectors-and-entry-points)
7. [Existing Security Controls](#existing-security-controls)
8. [Threat Mitigation Recommendations](#threat-mitigation-recommendations)
9. [Security Testing Requirements](#security-testing-requirements)
10. [Incident Response](#incident-response)
11. [Compliance and Regulatory Considerations](#compliance-and-regulatory-considerations)
12. [Review and Update Process](#review-and-update-process)
13. [References](#references)

---

## Executive Summary

[Provide a high-level overview of the system/feature and its key security concerns. This section should be understandable by non-technical stakeholders.]

**Purpose**: [What does this system/feature do?]

**Key Security Concerns**: 
- [Concern 1]
- [Concern 2]
- [Concern 3]

**Risk Level**: [High/Medium/Low]

---

## System Architecture Overview

### Component Description

[Describe the major components of the system and how they interact.]

```
[ASCII diagram or link to architecture diagram]
```

### Data Flow

[Describe how data flows through the system, from entry to exit.]

1. **Step 1**: [Description]
2. **Step 2**: [Description]
3. **Step 3**: [Description]

### Key Components

- **Component 1**: [Description and responsibilities]
- **Component 2**: [Description and responsibilities]
- **Component 3**: [Description and responsibilities]

### External Dependencies

- **Dependency 1**: [Name, version, purpose]
- **Dependency 2**: [Name, version, purpose]

---

## Assets and Data Classification

### Critical Assets

| Asset | Classification | Description | Security Requirement |
|-------|---------------|-------------|---------------------|
| [Asset Name] | [Public/Internal/Confidential/Secret] | [Description] | [What protection is needed] |

### Data Classification Levels

Define your organization's data classification levels:

- **Public**: Information that can be freely shared
- **Internal**: Information for internal use only
- **Confidential**: Sensitive information requiring protection
- **Secret**: Highly sensitive information (credentials, keys, etc.)

---

## Trust Boundaries

### Primary Boundaries

[Identify the boundaries where trust levels change]

1. **Boundary 1**: [Description]
   - **Trusted Side**: [Who/what is trusted]
   - **Untrusted Side**: [Who/what is untrusted]
   - **Controls**: [What protects this boundary]

2. **Boundary 2**: [Description]

### Trust Assumptions

[List assumptions about trust relationships]

- [Assumption 1]
- [Assumption 2]

---

## Threat Analysis (STRIDE)

Use the STRIDE methodology to identify threats:
- **S**poofing Identity
- **T**ampering with Data
- **R**epudiation
- **I**nformation Disclosure
- **D**enial of Service
- **E**levation of Privilege

### S - Spoofing Identity

| Threat ID | Description | Impact | Likelihood | Severity |
|-----------|-------------|--------|------------|----------|
| S-01 | [Threat description] | [High/Medium/Low] | [High/Medium/Low] | [Critical/High/Medium/Low] |

**Mitigations:**
- [Mitigation 1]
- [Mitigation 2]

### T - Tampering with Data

| Threat ID | Description | Impact | Likelihood | Severity |
|-----------|-------------|--------|------------|----------|
| T-01 | [Threat description] | [High/Medium/Low] | [High/Medium/Low] | [Critical/High/Medium/Low] |

**Mitigations:**
- [Mitigation 1]
- [Mitigation 2]

### R - Repudiation

| Threat ID | Description | Impact | Likelihood | Severity |
|-----------|-------------|--------|------------|----------|
| R-01 | [Threat description] | [High/Medium/Low] | [High/Medium/Low] | [Critical/High/Medium/Low] |

**Mitigations:**
- [Mitigation 1]
- [Mitigation 2]

### I - Information Disclosure

| Threat ID | Description | Impact | Likelihood | Severity |
|-----------|-------------|--------|------------|----------|
| I-01 | [Threat description] | [High/Medium/Low] | [High/Medium/Low] | [Critical/High/Medium/Low] |

**Mitigations:**
- [Mitigation 1]
- [Mitigation 2]

### D - Denial of Service

| Threat ID | Description | Impact | Likelihood | Severity |
|-----------|-------------|--------|------------|----------|
| D-01 | [Threat description] | [High/Medium/Low] | [High/Medium/Low] | [Critical/High/Medium/Low] |

**Mitigations:**
- [Mitigation 1]
- [Mitigation 2]

### E - Elevation of Privilege

| Threat ID | Description | Impact | Likelihood | Severity |
|-----------|-------------|--------|------------|----------|
| E-01 | [Threat description] | [High/Medium/Low] | [High/Medium/Low] | [Critical/High/Medium/Low] |

**Mitigations:**
- [Mitigation 1]
- [Mitigation 2]

---

## Attack Vectors and Entry Points

### External Attack Vectors

1. **Vector 1**
   - **Description**: [How could an attacker exploit this?]
   - **Example**: [Concrete example]
   - **Control**: [How is this prevented/detected?]

2. **Vector 2**
   - **Description**: [How could an attacker exploit this?]
   - **Example**: [Concrete example]
   - **Control**: [How is this prevented/detected?]

### Internal Attack Vectors

1. **Vector 1**
   - **Description**: [Insider threat or internal vulnerability]
   - **Example**: [Concrete example]
   - **Control**: [How is this prevented/detected?]

### Entry Points Summary

- [Entry point 1]
- [Entry point 2]
- [Entry point 3]

---

## Existing Security Controls

### Preventive Controls

| Control | Implementation | Effectiveness |
|---------|----------------|---------------|
| [Control Name] | [How it's implemented] | [High/Medium/Low] |

### Detective Controls

| Control | Implementation | Effectiveness |
|---------|----------------|---------------|
| [Control Name] | [How it's implemented] | [High/Medium/Low] |

### Corrective Controls

| Control | Implementation | Effectiveness |
|---------|----------------|---------------|
| [Control Name] | [How it's implemented] | [High/Medium/Low] |

### Gaps in Current Controls

- [Gap 1]
- [Gap 2]
- [Gap 3]

---

## Threat Mitigation Recommendations

### Critical Priority (Implement Immediately)

1. **[Recommendation Title]**
   - **Threat Mitigated**: [Threat IDs]
   - **Action**: [What needs to be done]
   - **Implementation**: [How to implement]
   - **Timeline**: [When to complete]
   - **Owner**: [Who is responsible]

### High Priority (Implement Within 1 Month)

2. **[Recommendation Title]**
   - **Threat Mitigated**: [Threat IDs]
   - **Action**: [What needs to be done]
   - **Implementation**: [How to implement]
   - **Timeline**: [When to complete]
   - **Owner**: [Who is responsible]

### Medium Priority (Implement Within 3 Months)

3. **[Recommendation Title]**
   - **Threat Mitigated**: [Threat IDs]
   - **Action**: [What needs to be done]
   - **Implementation**: [How to implement]
   - **Timeline**: [When to complete]
   - **Owner**: [Who is responsible]

### Low Priority (Ongoing Improvements)

4. **[Recommendation Title]**
   - **Threat Mitigated**: [Threat IDs]
   - **Action**: [What needs to be done]
   - **Implementation**: [How to implement]
   - **Timeline**: [When to complete]
   - **Owner**: [Who is responsible]

---

## Security Testing Requirements

### Required Security Tests

1. **[Test Category]**
   ```
   [Code example or test description]
   ```

2. **[Test Category]**
   - [Test description]
   - [Expected behavior]

### Security Testing Tools

- **[Tool Name]**: [Purpose and usage]
- **[Tool Name]**: [Purpose and usage]

### Testing Schedule

- **Unit Tests**: [When/how often]
- **Integration Tests**: [When/how often]
- **Penetration Tests**: [When/how often]
- **Security Audits**: [When/how often]

---

## Incident Response

### Security Incident Categories

1. **[Incident Type]**
   - Description: [What constitutes this incident type]
   - Response: [Initial response steps]

2. **[Incident Type]**
   - Description: [What constitutes this incident type]
   - Response: [Initial response steps]

### Incident Response Plan

1. **Detection**: [How incidents are detected]
2. **Containment**: [How to contain the incident]
3. **Investigation**: [How to investigate]
4. **Remediation**: [How to fix the issue]
5. **Communication**: [Who to notify and how]
6. **Post-Mortem**: [How to learn from the incident]

### Security Contacts

- **Security Team**: [Contact information]
- **Incident Response**: [Contact information]
- **On-Call**: [Contact information]

---

## Compliance and Regulatory Considerations

### Relevant Regulations

- **[Regulation Name]** (e.g., GDPR, HIPAA, PCI DSS)
  - **Requirements**: [What compliance is required]
  - **Implementation**: [How it's implemented]

### Compliance Requirements

- [Requirement 1]
- [Requirement 2]
- [Requirement 3]

### Audit Requirements

- **Frequency**: [How often]
- **Scope**: [What is audited]
- **Records**: [What records are maintained]

---

## Review and Update Process

### Review Cadence

- **Regular Reviews**: [Frequency]
- **Triggered Reviews**: [What triggers a review]

### Review Triggers

- [Trigger 1]
- [Trigger 2]
- [Trigger 3]

### Review Responsibilities

- **[Role]**: [Responsibilities in review process]
- **[Role]**: [Responsibilities in review process]

### Review Process

1. [Step 1]
2. [Step 2]
3. [Step 3]
4. [Step 4]
5. [Step 5]

### Metrics to Track

- [Metric 1]
- [Metric 2]
- [Metric 3]

---

## References

### Related Documentation

- [Document 1]: [Link or location]
- [Document 2]: [Link or location]

### Security Resources

- [Resource 1]: [Link]
- [Resource 2]: [Link]

### External Standards

- [Standard 1]: [Link]
- [Standard 2]: [Link]

---

## Document History

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | YYYY-MM-DD | [Name] | Initial creation |

---

## Notes

[Any additional notes or context that doesn't fit in the sections above]

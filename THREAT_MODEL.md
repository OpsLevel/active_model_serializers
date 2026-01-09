# Threat Model: Active Model Serializers

**Version:** 1.0  
**Last Updated:** 2024-01-09  
**Owner:** Security Team  
**Review Cycle:** Quarterly or upon significant architectural changes

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

Active Model Serializers (AMS) is a Ruby gem that provides a convention-based approach to JSON generation for Rails applications. As a serialization library that handles sensitive application data, it operates at a critical security boundary where internal data models are transformed into external API responses. This threat model identifies security risks associated with data serialization, information disclosure, and integration with Rails applications.

**Key Security Concerns:**
- Information disclosure through over-serialization
- Injection attacks via serializer code execution
- Dependency vulnerabilities
- Authorization bypass through improper serializer configuration
- Mass assignment vulnerabilities via deserialization

---

## System Architecture Overview

### Component Description

Active Model Serializers acts as a middleware layer between Rails models and JSON API responses:

```
┌─────────────────────────────────────────────────────────────┐
│                     Rails Application                        │
│  ┌──────────────┐      ┌─────────────────┐                 │
│  │ Controllers  │─────▶│  Serializers    │─────┐           │
│  └──────────────┘      └─────────────────┘     │           │
│         │                      │                 │           │
│         │                      ▼                 ▼           │
│         │              ┌─────────────────────────────┐      │
│         │              │ Active Model Serializers   │      │
│         │              │   (AMS Gem)                 │      │
│         │              └─────────────────────────┘          │
│         ▼                      │                             │
│  ┌──────────────┐             │                             │
│  │   Models     │◀────────────┘                             │
│  └──────────────┘                                           │
│         │                                                    │
│         ▼                                                    │
│  ┌──────────────┐                                           │
│  │   Database   │                                           │
│  └──────────────┘                                           │
└─────────────────────────────────────────────────────────────┘
                           │
                           ▼
                    ┌─────────────┐
                    │  JSON API   │
                    │  Response   │
                    └─────────────┘
                           │
                           ▼
                    ┌─────────────┐
                    │   Clients   │
                    │ (External)  │
                    └─────────────┘
```

### Data Flow

1. **Request Processing**: Client sends HTTP request to Rails controller
2. **Model Access**: Controller retrieves data from ActiveRecord models
3. **Serialization**: Models are passed to serializers (AMS)
4. **Transformation**: AMS converts models to structured JSON
5. **Response**: JSON response sent to client

### Key Components

- **Serializer Classes**: Define which attributes and associations to expose
- **Adapter Layer**: Formats output according to specifications (JSON:API, etc.)
- **Caching Layer**: Stores serialized responses for performance
- **Association Handling**: Manages nested resource serialization

---

## Assets and Data Classification

### Critical Assets

| Asset | Classification | Description | Security Requirement |
|-------|---------------|-------------|---------------------|
| User Data | Confidential/PII | Personal information, emails, phone numbers | Must not be exposed without authorization |
| Authentication Tokens | Secret | API keys, session tokens, OAuth tokens | Must never be serialized |
| Passwords/Hashes | Secret | Password hashes, encryption keys | Must never be serialized |
| Business Logic | Internal | Application models and relationships | Should be exposed selectively |
| Database Metadata | Internal | Schema information, internal IDs | Should be minimized in responses |
| API Keys | Secret | Third-party service credentials | Must never be serialized |
| Financial Data | Confidential | Payment information, transactions | Strict access control required |
| Healthcare Data | Confidential/PHI | Medical records (if applicable) | HIPAA compliance required |

### Data Classification Levels

- **Public**: Can be freely shared (e.g., published blog posts)
- **Internal**: For organizational use (e.g., internal IDs)
- **Confidential**: Sensitive business data (e.g., user emails, PII)
- **Secret**: Highly sensitive (e.g., passwords, tokens, keys)

---

## Trust Boundaries

### Primary Boundaries

1. **Application-to-Serializer**: Trust exists; application code determines what to serialize
2. **Serializer-to-Client**: **CRITICAL BOUNDARY** - untrusted external clients receive data
3. **Serializer-to-Cache**: Trust exists; cached data should match authorization context
4. **Dependency-to-Application**: External gems may contain vulnerabilities

### Trust Assumptions

- Application controllers properly authenticate and authorize users
- Serializer definitions are maintained by trusted developers
- Rails framework provides baseline security controls
- Database access is properly secured

---

## Threat Analysis (STRIDE)

### S - Spoofing Identity

| Threat ID | Description | Impact | Likelihood | Severity |
|-----------|-------------|--------|------------|----------|
| S-01 | Attacker impersonates another user to access their serialized data | High | Medium | **High** |
| S-02 | Serializer bypasses authentication checks in controllers | High | Low | **High** |
| S-03 | Cached serialized data served to wrong user | High | Medium | **High** |

**Mitigations:**
- Ensure serializers respect user context and authorization
- Implement user-specific cache keys
- Never expose authentication credentials in serialized output

### T - Tampering with Data

| Threat ID | Description | Impact | Likelihood | Severity |
|-----------|-------------|--------|------------|----------|
| T-01 | Malicious code injection in custom serializer methods | High | Low | **High** |
| T-02 | Deserialization attacks if accepting JSON input | Critical | Low | **Critical** |
| T-03 | Parameter pollution affecting serialization scope | Medium | Medium | **Medium** |

**Mitigations:**
- Code review all custom serializer methods
- Avoid eval() or dynamic code execution in serializers
- Validate and sanitize any inputs that affect serialization
- Use safe deserialization practices

### R - Repudiation

| Threat ID | Description | Impact | Likelihood | Severity |
|-----------|-------------|--------|------------|----------|
| R-01 | No audit trail for what data was serialized to whom | Medium | High | **Medium** |
| R-02 | Cannot prove which user accessed specific data through API | Medium | Medium | **Medium** |

**Mitigations:**
- Implement comprehensive API logging
- Log serialization context (user, timestamp, resources)
- Maintain audit trails for sensitive data access

### I - Information Disclosure

| Threat ID | Description | Impact | Likelihood | Severity |
|-----------|-------------|--------|------------|----------|
| I-01 | Over-serialization exposes sensitive attributes | High | High | **Critical** |
| I-02 | Stack traces in error responses reveal system internals | Medium | Medium | **Medium** |
| I-03 | Association loading exposes unauthorized related data | High | High | **Critical** |
| I-04 | Debug information in development leaks to production | Medium | Low | **Medium** |
| I-05 | Version information exposes known vulnerabilities | Low | High | **Low** |
| I-06 | Timing attacks reveal existence of resources | Low | Medium | **Low** |

**Mitigations:**
- Explicitly define attributes to serialize (whitelist approach)
- Never serialize password fields, tokens, or secrets
- Implement field-level authorization
- Use proper error handling without exposing internals
- Separate development and production configurations
- Implement consistent response times

### D - Denial of Service

| Threat ID | Description | Impact | Likelihood | Severity |
|-----------|-------------|--------|------------|----------|
| D-01 | N+1 queries from inefficient association serialization | Medium | High | **High** |
| D-02 | Recursive serialization causing infinite loops | High | Low | **High** |
| D-03 | Memory exhaustion from large serialization operations | High | Medium | **High** |
| D-04 | CPU exhaustion from complex custom serializer methods | Medium | Medium | **Medium** |
| D-05 | Cache flooding attacks | Medium | Low | **Medium** |

**Mitigations:**
- Use eager loading for associations
- Implement pagination for collection serialization
- Set depth limits for nested serialization
- Monitor resource usage and set timeouts
- Implement rate limiting at API level
- Cache serialized responses appropriately

### E - Elevation of Privilege

| Threat ID | Description | Impact | Likelihood | Severity |
|-----------|-------------|--------|------------|----------|
| E-01 | Serializer bypasses authorization checks | Critical | Medium | **Critical** |
| E-02 | Association serialization exposes unauthorized data | High | High | **Critical** |
| E-03 | Custom serializer methods execute with elevated privileges | High | Low | **High** |
| E-04 | Scope manipulation grants access to restricted resources | High | Medium | **High** |

**Mitigations:**
- Integrate authorization frameworks (Pundit, CanCanCan)
- Check permissions before serializing associations
- Scope queries to current user's authorized resources
- Regular security audits of serializer definitions
- Principle of least privilege in serializers

---

## Attack Vectors and Entry Points

### External Attack Vectors

1. **API Endpoints**
   - **Vector**: Manipulated query parameters requesting sensitive fields
   - **Example**: `GET /users/1?fields=password_digest,api_token`
   - **Control**: Whitelist allowed fields, ignore unauthorized requests

2. **Association Traversal**
   - **Vector**: Deep association chains accessing unauthorized data
   - **Example**: `GET /posts/1?include=user.private_messages.recipients`
   - **Control**: Limit association depth, check authorization at each level

3. **Mass Assignment via Parameters**
   - **Vector**: Malicious parameters affecting serialization behavior
   - **Example**: Parameters that change serializer context or scope
   - **Control**: Strong parameter filtering, validation

4. **Cache Poisoning**
   - **Vector**: Manipulated requests causing incorrect cached responses
   - **Example**: Cached admin view served to regular users
   - **Control**: User-context-aware cache keys

### Internal Attack Vectors

1. **Developer Errors**
   - **Vector**: Accidentally including sensitive fields in serializers
   - **Example**: `attributes :id, :name, :password_digest`
   - **Control**: Code review, automated security scanning

2. **Dependency Vulnerabilities**
   - **Vector**: Vulnerable versions of AMS or dependencies
   - **Example**: Known CVEs in gem dependencies
   - **Control**: Regular updates, dependency scanning

3. **Logic Bugs**
   - **Vector**: Conditional serialization logic bypassed
   - **Example**: `if admin?` check with flawed implementation
   - **Control**: Unit tests, integration tests, security tests

### Entry Points Summary

- Public API endpoints accepting serialized responses
- GraphQL endpoints (if integrated)
- Background job serialization
- Cached response generation
- Admin panel APIs
- Mobile app APIs
- Webhook payloads

---

## Existing Security Controls

### Preventive Controls

| Control | Implementation | Effectiveness |
|---------|----------------|---------------|
| Attribute Whitelisting | Explicit `attributes` declarations in serializers | High |
| Rails Parameter Filtering | Strong parameters in controllers | High |
| Authorization Integration | Can integrate with Pundit/CanCanCan | Medium (requires implementation) |
| Field Selection | Clients can't request arbitrary fields (by default) | Medium |
| JSON Schema Validation | Output format is predictable | Medium |

### Detective Controls

| Control | Implementation | Effectiveness |
|---------|----------------|---------------|
| Rails Logging | Basic request/response logging | Low (needs enhancement) |
| Exception Tracking | Rails error handling | Medium |
| Dependency Scanning | Manual via bundler-audit | Low (not automated) |

### Corrective Controls

| Control | Implementation | Effectiveness |
|---------|----------------|---------------|
| Gem Updates | Manual gem updates | Medium |
| Security Patches | Released via new gem versions | Medium |
| Rollback Capability | Rails migration/deployment rollback | High |

### Gaps in Current Controls

- No built-in field-level authorization
- Limited audit logging of data access
- No automated security testing framework
- No built-in rate limiting for serialization
- No automated dependency vulnerability scanning
- No formal security training for serializer development
- No automated detection of sensitive data exposure

---

## Threat Mitigation Recommendations

### Critical Priority (Implement Immediately)

1. **Implement Field-Level Authorization**
   - **Threat Mitigated**: I-01, I-03, E-01, E-02
   - **Action**: Integrate authorization checks in serializers
   - **Implementation**:
     ```ruby
     class UserSerializer < ActiveModel::Serializer
       attributes :id, :name, :email
       
       def email
         return nil unless current_user.admin? || current_user == object
         object.email
       end
     end
     ```

2. **Never Serialize Secrets**
   - **Threat Mitigated**: I-01, S-02
   - **Action**: Audit all serializers for exposed secrets
   - **Implementation**: Create blacklist of forbidden attributes
   - **Timeline**: 1 week

3. **Implement Security Testing**
   - **Threat Mitigated**: All
   - **Action**: Add automated security tests for serializers
   - **Implementation**: Test suite checking for sensitive field exposure
   - **Timeline**: 2 weeks

### High Priority (Implement Within 1 Month)

4. **Add Comprehensive Audit Logging**
   - **Threat Mitigated**: R-01, R-02
   - **Action**: Log all API requests with serialization context
   - **Implementation**: Rails middleware or serializer callbacks

5. **Implement Association Authorization**
   - **Threat Mitigated**: E-02, I-03
   - **Action**: Check permissions before serializing associations
   - **Implementation**: Authorization hooks in serializer relationships

6. **Optimize for Performance/DoS Prevention**
   - **Threat Mitigated**: D-01, D-02, D-03
   - **Action**: Implement eager loading, pagination, depth limits
   - **Implementation**: Default includes, max depth configuration

7. **Secure Cache Implementation**
   - **Threat Mitigated**: S-03, I-01
   - **Action**: User-context-aware cache keys
   - **Implementation**: Include user ID and permissions in cache keys

### Medium Priority (Implement Within 3 Months)

8. **Dependency Scanning Automation**
   - **Threat Mitigated**: All (dependency vulnerabilities)
   - **Action**: Automated security scanning in CI/CD
   - **Implementation**: bundler-audit, Dependabot, Snyk

9. **Security Documentation**
   - **Threat Mitigated**: All (developer awareness)
   - **Action**: Create security guidelines for serializer development
   - **Implementation**: Wiki or docs section with examples

10. **Rate Limiting**
    - **Threat Mitigated**: D-01, D-03, D-04
    - **Action**: Implement API rate limiting
    - **Implementation**: rack-attack or similar

### Low Priority (Ongoing Improvements)

11. **Security Training**
    - **Threat Mitigated**: All
    - **Action**: Train developers on serialization security
    - **Timeline**: Quarterly sessions

12. **Bug Bounty Program**
    - **Threat Mitigated**: All
    - **Action**: Consider security researcher engagement
    - **Timeline**: As resources permit

13. **Security Headers**
    - **Threat Mitigated**: Various
    - **Action**: Implement proper security headers for JSON APIs
    - **Implementation**: X-Content-Type-Options, etc.

---

## Security Testing Requirements

### Required Security Tests

1. **Serializer Security Tests**
   ```ruby
   test "should not expose password fields" do
     user = User.create!(password: 'secret')
     serializer = UserSerializer.new(user)
     json = serializer.as_json
     
     assert_not json.key?(:password)
     assert_not json.key?(:password_digest)
     assert_not json.key?(:password_hash)
   end
   ```

2. **Authorization Tests**
   - Test unauthorized access to user-specific data
   - Test cross-user data access
   - Test admin vs. regular user serialization differences

3. **Association Authorization Tests**
   - Test unauthorized association traversal
   - Test scope isolation between users

4. **Performance Tests**
   - Test N+1 query detection
   - Test serialization of large collections
   - Test recursive association limits

5. **Input Validation Tests**
   - Test parameter manipulation attempts
   - Test invalid field requests
   - Test malicious includes parameters

### Security Testing Tools

- **RSpec Security**: Custom matchers for security testing
- **Brakeman**: Static analysis security scanner for Rails
- **bundler-audit**: Check for vulnerable dependencies
- **Rails Security Checklist**: Periodic manual review

---

## Incident Response

### Security Incident Categories

1. **Data Exposure Incident**
   - Sensitive data leaked through serialization
   - Response: Identify affected users, audit logs, patch serializer

2. **Unauthorized Access**
   - User accessed data they shouldn't have
   - Response: Revoke access, audit extent, fix authorization

3. **Dependency Vulnerability**
   - CVE reported in AMS or dependencies
   - Response: Assess impact, update dependencies, test, deploy

### Incident Response Plan

1. **Detection**: Monitoring, alerts, user reports
2. **Containment**: Disable affected endpoints if necessary
3. **Investigation**: Audit logs, identify scope
4. **Remediation**: Patch, deploy, verify fix
5. **Communication**: Notify affected users if required
6. **Post-Mortem**: Document lessons learned, improve controls

### Security Contacts

- **Security Team**: security@example.com
- **Incident Response**: incidents@example.com
- **CVE Reporting**: Use GitHub Security Advisories

---

## Compliance and Regulatory Considerations

### Relevant Regulations

- **GDPR** (EU): Personal data handling, right to be forgotten
  - Ensure PII is only serialized with proper consent
  - Support data export and deletion

- **CCPA** (California): Consumer privacy rights
  - Similar requirements to GDPR

- **HIPAA** (Healthcare): Protected Health Information (PHI)
  - If serializing healthcare data, ensure compliance
  - Audit trails for all PHI access

- **PCI DSS** (Payment Cards): Payment card data security
  - Never serialize full card numbers or CVV
  - Use tokenization

- **SOX** (Financial): Sarbanes-Oxley for financial data
  - Audit trails for financial data access
  - Access controls on financial serializers

### Compliance Requirements

- Maintain audit logs for data access
- Implement data minimization (serialize only necessary fields)
- Support data portability (API export capabilities)
- Implement data retention policies
- Ensure encryption in transit (HTTPS)

---

## Review and Update Process

### Review Cadence

- **Quarterly Reviews**: Regular threat model updates
- **Post-Incident Reviews**: After security incidents
- **Post-Release Reviews**: After major version changes
- **Dependency Updates**: After security patches

### Review Triggers

- New features adding serialization capabilities
- Integration with new external systems
- Reported security vulnerabilities
- Changes in regulatory requirements
- Significant architecture changes

### Review Responsibilities

- **Security Team**: Lead threat model reviews
- **Development Team**: Identify new threats from features
- **Product Team**: Understand data sensitivity changes
- **DevOps Team**: Infrastructure security considerations

### Review Process

1. Schedule review meeting with stakeholders
2. Review changes since last update
3. Identify new threats and attack vectors
4. Update threat model document
5. Prioritize mitigation recommendations
6. Assign action items with timelines
7. Document decisions and rationale

### Metrics to Track

- Number of serializers with sensitive data
- Number of security incidents related to serialization
- Time to patch security vulnerabilities
- Test coverage for security tests
- Number of serializers with authorization checks

---

## References

### Related Documentation

- [CONTRIBUTING.md](CONTRIBUTING.md) - Contributing guidelines
- [README.md](README.md) - Project overview and documentation
- [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md) - Community guidelines
- [Threat Model Template](docs/THREAT_MODEL_TEMPLATE.md) - Template for future reviews

### Security Resources

- [OWASP Top 10](https://owasp.org/www-project-top-ten/)
- [OWASP API Security Top 10](https://owasp.org/www-project-api-security/)
- [Rails Security Guide](https://guides.rubyonrails.org/security.html)
- [Ruby Security Best Practices](https://ruby-doc.org/docs/ruby-doc-bundle/FAQ/FAQ.html)
- [STRIDE Threat Modeling](https://docs.microsoft.com/en-us/azure/security/develop/threat-modeling-tool-threats)

### Security Tools

- [Brakeman](https://brakemanscanner.org/) - Rails security scanner
- [bundler-audit](https://github.com/rubysec/bundler-audit) - Dependency vulnerability scanner
- [Dependabot](https://github.com/dependabot) - Automated dependency updates
- [Rails Security Checklist](https://github.com/eliotsykes/rails-security-checklist)

### External Standards

- [JSON:API Specification](https://jsonapi.org/)
- [CWE/SANS Top 25](https://www.sans.org/top25-software-errors/)
- [NIST Cybersecurity Framework](https://www.nist.gov/cyberframework)

---

## Document History

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | 2024-01-09 | Security Team | Initial threat model creation |

---

## Appendix: Threat Model Template

For future threat modeling exercises, use the template at [docs/THREAT_MODEL_TEMPLATE.md](docs/THREAT_MODEL_TEMPLATE.md).

---
title: Subprocessors
audience: organizations
revision: 2026-10-18
effective: 2026-10-18
notify: false
description: Third-party providers that process data for PyPI.
subprocessors:
  - name: Amazon Web Services
    category: Hosting and infrastructure
    purpose: Hosting and storage of user information
    data: Your information is stored on their servers.
    terms:
      - title: Data Processing Addendum
        url: https://aws.amazon.com/blogs/security/aws-gdpr-data-processing-addendum/
      - title: Privacy Notice
        url: https://aws.amazon.com/privacy/
  - name: Fastly
    category: Hosting and infrastructure
    purpose: Content delivery and hosting
    data: Your information passes through their servers.
    terms:
      - title: Data Processing Terms
        url: https://www.fastly.com/data-processing
      - title: Privacy Policy
        url: https://www.fastly.com/privacy/
  - name: Backblaze
    category: Hosting and infrastructure
    purpose: Storage of uploaded package files
    data: Files uploaded to PyPI are stored on their servers.
    terms:
      - title: Data Processing Addendum
        url: https://www.backblaze.com/company/policy/dpa-for-eea-eu-residents
      - title: Privacy Notice
        url: https://www.backblaze.com/company/policy/privacy
  - name: Google Cloud
    category: Hosting and infrastructure
    purpose: Download statistics (linehaul) and the BigQuery public dataset
    data: >-
      No personal information. Request time, request URL, TLS protocol and
      cipher, HTTP User-Agent and approximate country are sent to their
      servers; User-Agents are stored in aggregate form only.
    terms:
      - title: Cloud Data Processing Addendum
        url: https://cloud.google.com/terms/data-processing-addendum
      - title: Google Cloud Privacy Notice
        url: https://cloud.google.com/terms/cloud-privacy-notice
  - name: Stripe
    category: Payments
    purpose: Payment processing and billing information
    data: Your billing information is stored on their servers.
    terms:
      - title: Data Processing Agreement
        url: https://stripe.com/legal/dpa
      - title: Privacy Policy
        url: https://stripe.com/privacy
  - name: Sentry
    category: Monitoring
    purpose: Error reporting
    data: Some personal information may be stored on their servers.
    terms:
      - title: Data Processing Addendum
        url: https://sentry.io/legal/dpa/
      - title: Privacy Policy
        url: https://sentry.io/privacy/
  - name: Datadog
    category: Monitoring
    purpose: Metrics and application performance monitoring
    data: Some personal information may be stored on their servers.
    terms:
      - title: Data Processing Addendum
        url: https://www.datadoghq.com/legal/data-processing-addendum/
      - title: Privacy Policy
        url: https://www.datadoghq.com/legal/privacy/
  - name: Help Scout
    category: Support
    purpose: Support requests
    data: Some personal information may be stored on their servers.
    terms:
      - title: Data Processing Agreement
        url: https://www.helpscout.com/company/legal/dpa/
      - title: Privacy Policy
        url: https://www.helpscout.com/company/legal/privacy/
  - name: hCaptcha
    category: Security and abuse prevention
    purpose: Abuse protection on forms
    data: Some personal information may be processed on their servers.
    terms:
      - title: Privacy Policy
        url: https://www.hcaptcha.com/privacy
  - name: UserCheck
    category: Security and abuse prevention
    purpose: Email verification and fraud prevention
    data: Email addresses may be processed on their servers.
    terms:
      - title: Privacy Policy
        url: https://www.usercheck.com/legal/privacy
  - name: Have I Been Pwned
    category: Security and abuse prevention
    purpose: Breached-password checks
    data: No personal information is sent to their servers.
    terms:
      - title: Privacy Policy
        url: https://haveibeenpwned.com/Privacy
  - name: GitHub, GitLab, Google, ActiveState
    category: Sign-in and identity
    purpose: Identity providers for Trusted Publishing and optional account linking
    data: >-
      Only if you use these features: some personal information may be
      exchanged with the provider you choose.
    terms:
      - title: GitHub Privacy Statement
        url: https://docs.github.com/en/site-policy/privacy-policies/github-general-privacy-statement
      - title: GitLab Privacy Statement
        url: https://about.gitlab.com/privacy/
      - title: Google Privacy Policy
        url: https://policies.google.com/privacy
      - title: ActiveState Privacy Policy
        url: https://www.activestate.com/company/privacy-policy/
  - name: EthicalAds
    category: Advertising
    purpose: Advertising on pypi.org
    data: Some personal information may be processed on their servers.
    terms:
      - title: Privacy Policy
        url: https://www.ethicalads.io/privacy-policy/
---
# PyPI Subprocessors

The PSF uses these third-party services to operate PyPI. Each provider's use of
your information is subject to the terms linked in its row: the data processing
agreement between the provider and the PSF, where there is one, and the
provider's privacy policy.

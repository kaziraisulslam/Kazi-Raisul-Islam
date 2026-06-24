# Article 12: Automated Logging & Record-Keeping
## Regulatory Context
High-risk AI systems must automatically log events to enable traceability, risk identification, and post-market monitoring.

## Engineering Solution: Cryptographic Chaining
Traditional logs can be edited. We implement a **Hash-Chain Logging mechanism**. Each log entry includes the SHA-256 hash of the *previous* entry. This makes the log **tamper-evident**: if a single entry is modified, the entire chain breaks, immediately alerting auditors to unauthorized tampering.

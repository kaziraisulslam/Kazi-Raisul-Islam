# Article 9: Risk Management System
## Regulatory Requirement
A continuous, iterative risk management system must be established, documented, and maintained throughout the lifecycle of a high-risk AI system.

## Engineering Solution: Dynamic Risk Verification
Instead of a static paper risk assessment, this control systematically monitors known hazards. It evaluates both raw and residual risk scores based on operational metrics. If any critical hazard lacks active technical mitigation, the control triggers a `NON-COMPLIANT` state, serving as a gatekeeper within our automated deployment pipeline.

# Article 14: Human Oversight (HITL)
## Regulatory Context
High-risk AI systems must allow for human intervention. Fully autonomous decisions in high-stakes environments (like financial scoring) are prohibited without human verification.

## Engineering Solution: The "Confidence Gate"
We implement **Intentional Friction**. Our pipeline automatically calculates AI confidence. If it falls below a set threshold, the system triggers a **hard-stop**, forcing a human operator to sign off on the decision. This is recorded in an immutable `oversight_log.json` for auditors.

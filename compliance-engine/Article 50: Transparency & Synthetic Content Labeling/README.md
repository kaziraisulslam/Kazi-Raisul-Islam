# Article 50: Transparency Obligations for Synthetic Content
## Regulatory Requirement
Providers of generative AI systems must ensure that outputs (audio, image, video, or text) are marked in a machine-readable format and detectable as artificially generated or manipulated.

## Engineering Solution: Multi-Layered Tracking
In accordance with the finalized EU Code of Practice, this control checks for a **two-layer provenance configuration**:
1. An imperceptible watermark injected into the generation pipeline.
2. A cryptographic signature (C2PA standard alignment).

If either layer is missing or tampered with, the framework flags the asset as `NON-COMPLIANT` and triggers a downstream distribution block.

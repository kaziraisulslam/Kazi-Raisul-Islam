# compliance-engine/EU-AI-Act/Art-50-Transparency/control.py
import json
import os

def audit_synthetic_content(content_metadata):
    """
    Enforces Article 50(2) transparency requirements.
    Validates that synthetic/AI-generated outputs contain machine-readable markings.
    """
    has_watermark = content_metadata.get("watermark_detected", False)
    has_cryptographic_signature = content_metadata.get("c2pa_signature", False)
    
    # Under 2026 rules, a multi-layered approach (at least two indicators) is required
    is_compliant = has_watermark and has_cryptographic_signature
    
    artifact = {
        "article": "EU-AI-Act-Art-50",
        "status": "COMPLIANT" if is_compliant else "NON-COMPLIANT",
        "checks": {
            "imperceptible_watermark": has_watermark,
            "provenance_signature": has_cryptographic_signature
        },
        "content_type": content_metadata.get("content_type", "unknown"),
        "enforcement_action": "NONE" if is_compliant else "BLOCK_DISTRIBUTION"
    }
    
    os.makedirs('compliance-engine/EU-AI-Act/Art-50-Transparency/artifacts', exist_ok=True)
    with open('compliance-engine/EU-AI-Act/Art-50-Transparency/artifacts/artifact.json', 'w') as f:
        json.dump(artifact, f, indent=4)
        
    return artifact

if __name__ == "__main__":
    # Simulate scanning a generative text output longer than 200 tokens
    sample_payload = {
        "content_type": "text/markdown",
        "watermark_detected": True,
        "c2pa_signature": True
    }
    print(audit_synthetic_content(sample_payload))

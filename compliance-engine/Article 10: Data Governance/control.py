# compliance-engine/EU-AI-Act/Art-10-Data-Governance/control.py
import hashlib
import json
import os

def generate_lineage_hash(filepath):
    sha256_hash = hashlib.sha256()
    with open(filepath, "rb") as f:
        for byte_block in iter(lambda: f.read(65536), b""):
            sha256_hash.update(byte_block)
    return sha256_hash.hexdigest()

def run_governance_audit(dataset_path):
    try:
        # 1. Integrity Check (Lineage)
        data_hash = generate_lineage_hash(dataset_path)
        
        # 2. Bias Mitigation (Mock Scan)
        # In production, integrate with 'fairlearn' or 'aif360'
        bias_score = 0.02 # Example: 2% demographic variance
        
        artifact = {
            "article": "EU-AI-Act-Art-10",
            "status": "COMPLIANT" if bias_score < 0.05 else "NON-COMPLIANT",
            "integrity_hash": data_hash,
            "bias_score": bias_score,
            "data_source": dataset_path
        }
        
        with open('compliance-engine/EU-AI-Act/Art-10-Data-Governance/artifact.json', 'w') as f:
            json.dump(artifact, f, indent=4)
        return artifact
    except Exception as e:
        return {"status": "ERROR", "error": str(e)}

if __name__ == "__main__":
    print(run_governance_audit("sample_data.csv"))

# compliance-engine/EU-AI-Act/Art-14-Human-Oversight/control.py
import json
import datetime
import os

def check_human_gate(confidence_score, threshold=0.85):
    """
    Enforces Human-in-the-Loop (HITL) for low-confidence AI decisions.
    Maps to Art 14: Human Oversight requirements.
    """
    is_compliant = confidence_score >= threshold
    
    status = "APPROVED" if is_compliant else "REQUIRES_HUMAN_REVIEW"
    
    artifact = {
        "article": "EU-AI-Act-Art-14",
        "timestamp": str(datetime.datetime.now()),
        "confidence_score": confidence_score,
        "threshold": threshold,
        "action": status,
        "oversight_required": not is_compliant
    }
    
    # Save the decision record for the auditor
    os.makedirs('compliance-engine/EU-AI-Act/Art-14-Human-Oversight/artifacts', exist_ok=True)
    with open('compliance-engine/EU-AI-Act/Art-14-Human-Oversight/artifacts/oversight_log.json', 'w') as f:
        json.dump(artifact, f, indent=4)
        
    return artifact

if __name__ == "__main__":
    # Test: If model provides 0.72 confidence, it triggers the gate
    print(check_human_gate(0.72))

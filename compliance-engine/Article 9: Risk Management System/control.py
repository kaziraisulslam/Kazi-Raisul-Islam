# compliance-engine/EU-AI-Act/Art-9-Risk-Management/control.py
import json
import os
import datetime

def evaluate_lifecycle_risk(system_hazards):
    """
    Implements Article 9 continuous risk management.
    Identifies, estimates, and ensures mitigation of foreseeable risks.
    """
    remediation_required = False
    evaluated_hazards = []

    for hazard in system_hazards:
        # Calculate raw risk score (Impact x Probability)
        raw_score = hazard["impact"] * hazard["probability"]
        
        # Determine if residual risk is acceptable under Article 9(4)
        status = "ACCEPTABLE"
        if raw_score > 12 and not hazard["mitigation_active"]:
            status = "UNACCEPTABLE_ACTION_REQUIRED"
            remediation_required = True
            
        evaluated_hazards.append({
            "hazard_id": hazard["id"],
            "risk_score": raw_score,
            "residual_status": status
        })

    artifact = {
        "article": "EU-AI-Act-Art-9",
        "timestamp": str(datetime.datetime.now()),
        "status": "NON-COMPLIANT" if remediation_required else "COMPLIANT",
        "lifecycle_stage": "Post-Market_Monitoring_Ready",
        "hazard_matrix": evaluated_hazards
    }

    os.makedirs('compliance-engine/EU-AI-Act/Art-9-Risk-Management/artifacts', exist_ok=True)
    with open('compliance-engine/EU-AI-Act/Art-9-Risk-Management/artifacts/artifact.json', 'w') as f:
        json.dump(artifact, f, indent=4)
        
    return artifact

if __name__ == "__main__":
    # Test suite sample data mocking standard system hazards
    sample_hazards = [
        {"id": "HAZ-01", "description": "Biased credit outcomes", "impact": 5, "probability": 3, "mitigation_active": True},
        {"id": "HAZ-02", "description": "Unauthorised access to pipeline", "impact": 4, "probability": 4, "mitigation_active": False}
    ]
    print(evaluate_lifecycle_risk(sample_hazards))

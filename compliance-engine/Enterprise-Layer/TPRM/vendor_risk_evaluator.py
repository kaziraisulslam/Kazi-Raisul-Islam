# compliance-engine/Enterprise-Layer/TPRM/vendor_risk_evaluator.py
import json
import os

def evaluate_vendor_risk(vendor_manifest):
    """
    Automated Third-Party Risk Management (TPRM) evaluator for AI vendors.
    Cross-references vendor features against EU AI Act mandatory requirements.
    """
    mandatory_articles = ["Art_9_Risk", "Art_10_Data", "Art_11_Docs", "Art_12_Logs", "Art_14_Human", "Art_15_Robustness"]
    provided_evidence = vendor_manifest.get("compliance_evidence", {})
    
    missing_controls = [art for art in mandatory_articles if not provided_evidence.get(art, False)]
    
    # Calculate operational risk scoring
    base_score = 100
    deduction_per_missing = 15
    final_score = max(0, base_score - (len(missing_controls) * deduction_per_missing))
    
    status = "APPROVED_FOR_INTEGRATION"
    if final_score < 70 or "Art_10_Data" in missing_controls:
        status = "REJECTED_COMPLIANCE_GAP"
        
    assessment = {
        "vendor_name": vendor_manifest.get("vendor_name", "Unknown"),
        "timestamp": "2026-06-25T22:00:00Z",
        "vendor_risk_score": final_score,
        "onboarding_status": status,
        "missing_regulatory_controls": missing_controls,
        "action_required": "None" if status == "APPROVED_FOR_INTEGRATION" else "Review missing telemetry configurations"
    }
    
    os.makedirs('compliance-engine/Enterprise-Layer/TPRM/artifacts', exist_ok=True)
    with open('compliance-engine/Enterprise-Layer/TPRM/artifacts/tprm_assessment.json', 'w') as f:
        json.dump(assessment, f, indent=4)
        
    return assessment

if __name__ == "__main__":
    sample_vendor = {
        "vendor_name": "Alpha-Agentic-LLM",
        "compliance_evidence": {
            "Art_9_Risk": True,
            "Art_10_Data": True,
            "Art_11_Docs": False,
            "Art_12_Logs": True,
            "Art_14_Human": True,
            "Art_15_Robustness": False
        }
    }
    print(json.dumps(evaluate_vendor_risk(sample_vendor), indent=2))

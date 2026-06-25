# compliance-engine/Enterprise-Layer/Integration/itsm_bridge.py
import json

def generate_itsm_ticket(ccm_alert_payload):
    """
    Transforms a technical compliance drift event into an enterprise-ready Jira/ServiceNow schema.
    """
    if ccm_alert_payload.get("status") != "CRITICAL_ALERT":
        return {"status": "NO_ACTION_REQUIRED"}
        
    violations_summary = "; ".join(ccm_alert_payload.get("violations", []))
    
    # Format according to standard corporate IT service schemas
    jira_ticket = {
        "fields": {
            "project": {"key": "GRC"},
            "summary": f"🚨 REGULATORY COMPLIANCE FAILURE: AI Model Drift Detected",
            "description": f"Automated CCM testing triggered compliance faults.\nDetails: {violations_summary}",
            "priority": {"name": "Highest"},
            "labels": ["EU-AI-Act", "Continuous-Auditing", "Automated-Escalation"],
            "customfield_10201": "Authority-Digitalization-Romania-Audit-Scope",
            "assignment_group": "AI Engineering Emergency Response"
        }
    }
    
    return jira_ticket

if __name__ == "__main__":
    mock_alert = {
        "status": "CRITICAL_ALERT",
        "violations": ["Bias drift detected: 0.07 exceeds legal limit of 0.05 (Art 10)"]
    }
    print(json.dumps(generate_itsm_ticket(mock_alert), indent=2))

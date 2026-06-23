import json
import datetime

# Mock function: In a real scenario, this gets the AI's confidence score
def get_ai_prediction():
    return {"result": "Approve_Loan", "confidence": 0.72}

def run_human_oversight_gate(threshold=0.85):
    prediction = get_ai_prediction()
    confidence = prediction['confidence']
    
    # Audit log entry for Article 14
    audit_event = {
        "timestamp": str(datetime.datetime.now()),
        "control_id": "ART-14-HITL",
        "action": "Confidence_Threshold_Check",
        "confidence_score": confidence,
        "required_threshold": threshold
    }

    if confidence < threshold:
        audit_event["status"] = "PENDING_HUMAN_REVIEW"
        print(f"[GATE LOCKED] Confidence {confidence} < {threshold}. Human review required.")
        # Logic here would trigger a Slack/Email notification or a Jira ticket
    else:
        audit_event["status"] = "AUTO_APPROVED"
        print(f"[GATE OPEN] Confidence {confidence} >= {threshold}. Processing allowed.")

    # Save artifact
    with open('compliance-engine/samples/hitl_audit_log.json', 'w') as f:
        json.dump(audit_event, f, indent=4)

if __name__ == "__main__":
    run_human_oversight_gate()

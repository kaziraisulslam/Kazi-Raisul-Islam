import json
import time

def calculate_priority_and_routing(violations):
    """
    Stage 2 (Triage & Routing): Pure logic engine to evaluate impact severity.
    Determines ITSM Priority (P1-P4) and targets the correct routing queue.
    """
    if not violations:
        return {"name": "Low"}, "General IT Ops Support"
        
    has_critical_violation = False
    has_data_violation = False
    
    for violation in violations:
        v_upper = violation.upper()
        if "ART 10" in v_upper or "BIAS" in v_upper or "DATA" in v_upper:
            has_data_violation = True
        if "ART 15" in v_upper or "LATENCY" in v_upper or "ROBUSTNESS" in v_upper:
            has_critical_violation = True
        if "ART 9" in v_upper or "CRITICAL_ALERT" in v_upper:
            has_critical_violation = True

    # Assign priority levels and routing groups based on corporate compliance rules
    if has_data_violation or has_critical_violation:
        return {"name": "Highest"}, "AI Engineering Emergency Response"
    else:
        return {"name": "Medium"}, "Tier-2 Application Support"

def generate_itsm_ticket(ccm_alert_payload):
    """
    Stage 1 & 3: Master ingestion function that converts compliance telemetry
    into a standardized ServiceNow / Jira Enterprise Incident Schema.
    """
    status = ccm_alert_payload.get("status", "OPERATIONAL")
    
    if status != "CRITICAL_ALERT":
        return {"status": "NO_ACTION_REQUIRED"}
        
    violations = ccm_alert_payload.get("violations", [])
    violations_summary = "; ".join(violations) if violations else "Unspecified structural drift."
    
    # Execute Stage 2 triage routing
    priority, assignment_group = calculate_priority_and_routing(violations)
    
    # Construct corporate schema representing ServiceNow Incident / Jira Task structures
    jira_ticket = {
        "status": "INCIDENT_CREATED",
        "fields": {
            "project": {
                "key": "AIA",
                "name": "AI Act Compliance Automation"
            },
            "summary": "🚨 REGULATORY COMPLIANCE FAILURE: Automated Core Control Drift Detected",
            "description": (
                f"SYSTEM TELEMETRY ALERT:\n"
                f"Continuous Control Monitoring (CCM) has detected operational threshold drift.\n\n"
                f"Active Violations:\n- {violations_summary}\n\n"
                f"Action Required: Immediately inspect model training pipeline or serving endpoint."
            ),
            "priority": priority,
            "assignment_group": assignment_group,
            "labels": [
                "EU-AI-Act",
                "Continuous-Auditing",
                "Automated-Escalation"
            ],
            # Stage 3: Mandatory regulatory audit metadata tracking fields
            "customfield_10201": "Authority-Digitalization-Romania-Audit-Scope",
            "sla_target_hours": 2 if priority["name"] == "Highest" else 8,
            "created_at": int(time.time())
        }
    }
    
    return jira_ticket

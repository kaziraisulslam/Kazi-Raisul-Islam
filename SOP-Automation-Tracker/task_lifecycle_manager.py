# SOP-Automation-Tracker/src/task_lifecycle_manager.py
import json
import time

class ManufacturingSOPTracker:
    def __init__(self):
        # Explicit ITIL / Industry 4.0 Standard Operating States
        self.valid_states = ["NEW", "ASSIGNED", "PROCESSING", "RESOLVED", "AUDIT_CLOSED"]
        
    def triage_incident(self, event_description, risk_category):
        """
        Ingests a floor-level manufacturing operational error or equipment deviation,
        calculates response urgency, and injects SEMI E187 security audit markers.
        """
        timestamp = int(time.time())
        risk_upper = risk_category.upper()
        
        # Calculate industrial priority levels dynamically
        if risk_upper in ["CYBERSECURITY", "SEMI_E187_DEVIATION", "NETWORK_CRITICAL"]:
            priority = "P1_CRITICAL"
            assignment_group = "Industrial Control Systems (ICS) Security Team"
            sla_target_minutes = 30
        elif risk_upper in ["EQUIPMENT_WEAR", "LOGISTICS_DELAY"]:
            priority = "P3_MEDIUM"
            assignment_group = "Mechanical Preventative Maintenance"
            sla_target_minutes = 240
        else:
            priority = "P4_LOW"
            assignment_group = "General Floor Operations Support"
            sla_target_minutes = 480
            
        # Construct the formal operational task payload
        task_incident = {
            "incident_id": f"INC-{timestamp}",
            "current_state": "NEW",
            "metadata": {
                "reported_at": timestamp,
                "urgency_tier": priority,
                "targeted_queue": assignment_group,
                "sla_limit_minutes": sla_target_minutes,
                "semi_e187_compliant_flag": True if risk_upper == "SEMI_E187_DEVIATION" else False
            },
            "audit_trail": [
                {"state": "NEW", "transition_time": timestamp, "operator_note": "System alert logged via edge instrumentation."}
            ],
            "log_payload": event_description
        }
        
        return task_incident

    def advance_state(self, current_incident, next_state, notes=""):
        """Enforces a strict state machine architecture to protect compliance trails."""
        next_state_upper = next_state.upper()
        if next_state_upper not in self.valid_states:
            raise ValueError(f"Invalid corporate status state: {next_state_upper}")
            
        current_incident["current_state"] = next_state_upper
        current_incident["audit_trail"].append({
            "state": next_state_upper,
            "transition_time": int(time.time()),
            "operator_note": notes
        })
        return current_incident

if __name__ == "__main__":
    tracker = ManufacturingSOPTracker()
    # Mocking a physical cyber security breach incident on an industrial endpoint
    breach_event = tracker.triage_incident(
        event_description="Unmapped TCP connection detected on PLC Controller Aisle 4",
        risk_category="SEMI_E187_DEVIATION"
    )
    print("🚀 Auto-Triaged Incident Payload Structure:\n")
    print(json.dumps(breach_event, indent=4))

# compliance-engine/EU-AI-Act/Art-12-Logging/control.py
import json
import hashlib
import datetime
import os

class ComplianceLogger:
    def __init__(self, log_file='compliance-engine/EU-AI-Act/Art-12-Logging/artifacts/audit_trail.log'):
        self.log_file = log_file
        self.last_hash = "0" * 64 # Genesis hash

    def log_event(self, event_data):
        timestamp = datetime.datetime.now().isoformat()
        # Create a chain: hash(event + previous_hash)
        payload = json.dumps({"timestamp": timestamp, "data": event_data, "prev_hash": self.last_hash})
        current_hash = hashlib.sha256(payload.encode()).hexdigest()
        
        log_entry = {"hash": current_hash, "payload": payload}
        
        with open(self.log_file, "a") as f:
            f.write(json.dumps(log_entry) + "\n")
            
        self.last_hash = current_hash
        return current_hash

# Example usage
if __name__ == "__main__":
    logger = ComplianceLogger()
    logger.log_event({"action": "AI_INFERENCE", "model_id": "credit-score-v1", "user_id": "USR-99"})
    print("Event logged with cryptographic chain.")

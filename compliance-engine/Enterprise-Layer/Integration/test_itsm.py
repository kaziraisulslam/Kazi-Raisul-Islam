import unittest
import os
import sys

# Inject directory path to allow absolute imports in CI/CD environments
current_dir = os.path.dirname(os.path.abspath(__file__))
if current_dir not in sys.path:
    sys.path.insert(0, current_dir)

from itsm_bridge import generate_itsm_ticket

class TestITSMBridge(unittest.TestCase):
    def test_no_action_for_operational_state(self):
        """Validates that operational telemetry does not create noisy IT support tickets."""
        payload = {"status": "OPERATIONAL"}
        result = generate_itsm_ticket(payload)
        self.assertEqual(result["status"], "NO_ACTION_REQUIRED")

    def test_jira_ticket_generation_on_failure(self):
        """Validates that a critical compliance alert successfully builds a structured Jira ticket payload."""
        payload = {
            "status": "CRITICAL_ALERT",
            "violations": ["Latency 300ms exceeds robustness limit (Art 15)"]
        }
        result = generate_itsm_ticket(payload)
        
        # Verify enterprise schema values are populated correctly
        self.assertEqual(result["fields"]["priority"]["name"], "Highest")
        self.assertIn("EU-AI-Act", result["fields"]["labels"])
        self.assertIn("Latency 300ms", result["fields"]["description"])

if __name__ == '__main__':
    unittest.main()

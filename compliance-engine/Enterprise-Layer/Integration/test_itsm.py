import unittest
import os
import sys

# Dynamic path injection to find itsm_bridge without relative imports
current_dir = os.path.dirname(os.path.abspath(__file__))
if current_dir not in sys.path:
    sys.path.insert(0, current_dir)

from itsm_bridge import generate_itsm_ticket

class TestITSMBridge(unittest.TestCase):
    def test_no_action_for_operational_state(self):
        payload = {"status": "OPERATIONAL"}
        result = generate_itsm_ticket(payload)
        self.assertEqual(result["status"], "NO_ACTION_REQUIRED")

    def test_jira_ticket_generation_on_failure(self):
        payload = {
            "status": "CRITICAL_ALERT",
            "violations": ["Latency 300ms exceeds robustness limit (Art 15)"]
        }
        result = generate_itsm_ticket(payload)
        self.assertEqual(result["fields"]["priority"]["name"], "Highest")
        self.assertIn("EU-AI-Act", result["fields"]["labels"])

if __name__ == '__main__':
    unittest.main()

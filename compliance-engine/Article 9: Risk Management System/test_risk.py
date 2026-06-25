import unittest
import os
import sys

# Dynamic path injection to find control safely in an isolated process
current_dir = os.path.dirname(os.path.abspath(__file__))
if current_dir not in sys.path:
    sys.path.insert(0, current_dir)

from control import evaluate_lifecycle_risk

class TestArt9(unittest.TestCase):
    def test_acceptable_residual_risk(self):
        hazards = [{"id": "HAZ-01", "impact": 3, "probability": 2, "mitigation_active": False}]
        result = evaluate_lifecycle_risk(hazards)
        self.assertEqual(result["status"], "COMPLIANT")
        
    def test_unacceptable_risk_triggers_fail(self):
        hazards = [{"id": "HAZ-02", "impact": 5, "probability": 4, "mitigation_active": False}]
        result = evaluate_lifecycle_risk(hazards)
        self.assertEqual(result["status"], "NON-COMPLIANT")

if __name__ == '__main__':
    unittest.main()

# compliance-engine/EU-AI-Act/Art-9-Risk-Management/test_risk.py
import unittest
from .control import evaluate_lifecycle_risk

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

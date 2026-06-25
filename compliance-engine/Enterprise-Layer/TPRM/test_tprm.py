import unittest
import os
import sys

# Inject directory path to allow absolute imports in CI/CD environments
current_dir = os.path.dirname(os.path.abspath(__file__))
if current_dir not in sys.path:
    sys.path.insert(0, current_dir)

from vendor_risk_evaluator import evaluate_vendor_risk

class TestTPRM(unittest.TestCase):
    def test_vendor_approval(self):
        """Validates that a fully compliant AI vendor passes onboarding."""
        vendor = {
            "vendor_name": "Compliant-AI-Vendor",
            "compliance_evidence": {
                "Art_9_Risk": True, "Art_10_Data": True, "Art_11_Docs": True,
                "Art_12_Logs": True, "Art_14_Human": True, "Art_15_Robustness": True
            }
        }
        result = evaluate_vendor_risk(vendor)
        self.assertEqual(result["onboarding_status"], "APPROVED_FOR_INTEGRATION")

    def test_vendor_rejection_on_data_governance(self):
        """Ensures vendors failing Article 10 Data Governance are blocked."""
        vendor = {
            "vendor_name": "NonCompliant-AI-Vendor",
            "compliance_evidence": {
                "Art_10_Data": False
            }
        }
        result = evaluate_vendor_risk(vendor)
        self.assertEqual(result["onboarding_status"], "REJECTED_COMPLIANCE_GAP")

if __name__ == '__main__':
    unittest.main()

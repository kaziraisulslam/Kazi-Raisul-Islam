# compliance-engine/Enterprise-Layer/TPRM/test_tprm.py
import unittest
from .vendor_risk_evaluator import evaluate_vendor_risk

class TestTPRM(unittest.TestCase):
    def test_vendor_approval(self):
        # A vendor that complies with all requirements
        vendor = {
            "vendor_name": "Compliant-AI",
            "compliance_evidence": {
                "Art_9_Risk": True, "Art_10_Data": True, "Art_11_Docs": True,
                "Art_12_Logs": True, "Art_14_Human": True, "Art_15_Robustness": True
            }
        }
        result = evaluate_vendor_risk(vendor)
        self.assertEqual(result["onboarding_status"], "APPROVED_FOR_INTEGRATION")

    def test_vendor_rejection_on_data_governance(self):
        # A vendor missing critical Art 10 compliance must fail
        vendor = {"compliance_evidence": {"Art_10_Data": False}}
        result = evaluate_vendor_risk(vendor)
        self.assertEqual(result["onboarding_status"], "REJECTED_COMPLIANCE_GAP")

if __name__ == '__main__':
    unittest.main()

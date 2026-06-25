# compliance-engine/Article 50: Transparency & Synthetic Content Labeling/test_transparency.py
import unittest
import os
import sys

# Dynamic path injection to find control safely in an isolated process
current_dir = os.path.dirname(os.path.abspath(__file__))
if current_dir not in sys.path:
    sys.path.insert(0, current_dir)

from control import audit_synthetic_content

class TestArt50(unittest.TestCase):
    def test_compliant_multi_layer_marking(self):
        """Validates that a synthetic asset with both watermark and signature passes."""
        payload = {"content_type": "image/jpeg", "watermark_detected": True, "c2pa_signature": True}
        result = audit_synthetic_content(payload)
        self.assertEqual(result["status"], "COMPLIANT")
        
    def test_non_compliant_missing_signature(self):
        """Ensures assets missing core cryptographic provenance signatures are blocked."""
        payload = {"content_type": "text/html", "watermark_detected": True, "c2pa_signature": False}
        result = audit_synthetic_content(payload)
        self.assertEqual(result["status"], "NON-COMPLIANT")
        self.assertEqual(result["enforcement_action"], "BLOCK_DISTRIBUTION")

if __name__ == '__main__':
    unittest.main()

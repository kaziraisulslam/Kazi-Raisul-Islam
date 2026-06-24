# compliance-engine/EU-AI-Act/Art-10-Data-Governance/tests.py
import unittest
import os
from control import run_governance_audit

class TestArt10(unittest.TestCase):
    def test_audit_missing_file(self):
        result = run_governance_audit("fake_file.csv")
        self.assertEqual(result["status"], "ERROR")

if __name__ == '__main__':
    unittest.main()

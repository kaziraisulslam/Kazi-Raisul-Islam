# compliance-engine/EU-AI-Act/Art-15-Accuracy-Robustness/tests.py
import unittest
from control import run_robustness_test

class TestArt15(unittest.TestCase):
    def test_robustness_threshold(self):
        result = run_robustness_test(0.95)
        self.assertEqual(result["robustness_status"], "PASS")

if __name__ == '__main__':
    unittest.main()

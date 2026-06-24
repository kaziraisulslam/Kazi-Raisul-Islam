# compliance-engine/EU-AI-Act/Art-14-Human-Oversight/tests.py
import unittest
from control import check_human_gate

class TestArt14(unittest.TestCase):
    def test_gate_triggers(self):
        result = check_human_gate(0.50)
        self.assertEqual(result["action"], "REQUIRES_HUMAN_REVIEW")

if __name__ == '__main__':
    unittest.main()

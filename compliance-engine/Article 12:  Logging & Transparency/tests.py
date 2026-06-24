# compliance-engine/EU-AI-Act/Art-12-Logging/tests.py
import unittest
import os
from control import ComplianceLogger

class TestArt12(unittest.TestCase):
    def test_log_creation(self):
        logger = ComplianceLogger('test.log')
        logger.log_event({"test": "data"})
        self.assertTrue(os.path.exists('test.log'))
        os.remove('test.log')

if __name__ == '__main__':
    unittest.main()

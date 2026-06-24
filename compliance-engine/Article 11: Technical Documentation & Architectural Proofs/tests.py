import unittest
from control import verify_architecture_compliance

class TestArt11(unittest.TestCase):
    def test_compliance_status(self):
        # We test that our artifact keys are present
        res = verify_architecture_compliance()
        self.assertIn("status", res)

if __name__ == '__main__':
    unittest.main()

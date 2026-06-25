import unittest
import os
import sys

# Inject directory path to allow absolute imports in CI/CD environments
current_dir = os.path.dirname(os.path.abspath(__file__))
if current_dir not in sys.path:
    sys.path.insert(0, current_dir)

from drift_monitor import monitor_model_telemetry

class TestCCM(unittest.TestCase):
    def test_operational_telemetry(self):
        """Ensures that normal metrics do not trigger false compliance alerts."""
        result = monitor_model_telemetry(current_bias_score=0.02, current_latency_ms=150.0)
        self.assertEqual(result["status"], "OPERATIONAL")

    def test_critical_drift_alert(self):
        """Ensures that telemetry drifting past legal limits triggers an immediate alert."""
        result = monitor_model_telemetry(current_bias_score=0.08, current_latency_ms=100.0)
        self.assertEqual(result["status"], "CRITICAL_ALERT")
        self.assertTrue(any("Bias drift" in violation for violation in result["violations"]))

if __name__ == '__main__':
    unittest.main()

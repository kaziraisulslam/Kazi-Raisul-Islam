import unittest
import os

def run_all_compliance_tests():
    """
    Discovers and executes all tests in the subdirectories.
    This creates a single 'Audit Result' for the entire engine.
    """
    # Start discovery from the current directory
    loader = unittest.TestLoader()
    suite = loader.discover(start_dir='.', pattern='test_*.py')
    
    # Run the tests
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)
    
    # Exit with appropriate status code for CI/CD pipelines (e.g., GitHub Actions)
    if result.wasSuccessful():
        print("\n[SUCCESS] All compliance controls are valid.")
        exit(0)
    else:
        print("\n[FAILURE] Compliance gaps detected. Please review artifacts.")
        exit(1)

if __name__ == "__main__":
    run_all_compliance_tests()

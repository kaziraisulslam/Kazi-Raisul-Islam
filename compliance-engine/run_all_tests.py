# compliance-engine/run_all_tests.py
import unittest
import os

def run_all_compliance_tests():
    """
    Crawls the entire repository to dynamically discover and execute 
    all compliance and enterprise integration tests.
    """
    loader = unittest.TestLoader()
    suite = unittest.TestSuite()

    # Walk through all directories recursively
    for root, dirs, files in os.walk('.'):
        for file in files:
            if file.startswith('test_') and file.endswith('.py'):
                # Force discovery on the specific file in its specific folder
                tests = loader.discover(start_dir=root, pattern=file)
                suite.addTests(tests)
    
    # Run the aggregated suite
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)
    
    if result.wasSuccessful():
        print("\n[SUCCESS] All framework and enterprise controls passed.")
        exit(0)
    else:
        print("\n[FAILURE] Critical gaps detected in compliance telemetry.")
        exit(1)

if __name__ == "__main__":
    run_all_compliance_tests()

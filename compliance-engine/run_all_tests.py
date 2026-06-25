import unittest
import os
import sys

def run_all_compliance_tests():
    """
    Crawls the entire repository to dynamically discover and execute 
    all compliance and enterprise integration tests.
    """
    # Ensure root directories are in the path
    root_dir = os.path.dirname(os.path.abspath(__file__))
    if root_dir not in sys.path:
        sys.path.insert(0, root_dir)

    loader = unittest.TestLoader()
    suite = unittest.TestSuite()

    # Walk through all directories recursively to find tests
    for root, dirs, files in os.walk('.'):
        for file in files:
            if file.startswith('test_') and file.endswith('.py'):
                # Add current directory to path so tests can resolve imports locally
                abs_root = os.path.abspath(root)
                if abs_root not in sys.path:
                    sys.path.insert(0, abs_root)
                
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

# compliance-engine/run_all_tests.py
import unittest
import os
import sys

def run_all_compliance_tests():
    """
    Crawls the entire repository, dynamically injects every subfolder 
    into the Python path, and executes all compliance tests safely.
    """
    # 1. Get absolute path of the engine root
    root_dir = os.path.dirname(os.path.abspath(__file__))
    
    # 2. Walk through all directories and force inject them into sys.path
    # This allows tests inside folders to find their sibling control files easily
    for root, dirs, files in os.walk(root_dir):
        if root not in sys.path:
            sys.path.insert(0, root)

    # 3. Initialize the Test Loader
    loader = unittest.TestLoader()
    suite = unittest.TestSuite()

    # 4. Discover tests explicitly using absolute directory paths
    for root, dirs, files in os.walk(root_dir):
        for file in files:
            if file.startswith('test_') and file.endswith('.py'):
                # Load the specific test file from its specific absolute folder path
                discovered_tests = loader.discover(start_dir=root, pattern=file)
                suite.addTests(discovered_tests)
    
    # 5. Execute the completed test suite
    print(f"🚀 Running all discovered compliance and enterprise controls...")
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)
    
    # 6. Exit with clean codes for GitHub Actions CI/CD
    if result.wasSuccessful():
        print("\n[SUCCESS] All compliance engine and enterprise controls passed perfectly.")
        exit(0)
    else:
        print("\n[FAILURE] Framework errors or compliance gaps detected. Check logs.")
        exit(1)

if __name__ == "__main__":
    run_all_compliance_tests()

# compliance-engine/run_all_tests.py
import os
import sys
import subprocess

def run_all_compliance_tests():
    """
    Finds every test file recursively and executes it in an isolated 
    subprocess inside its native directory to eliminate import path conflicts.
    """
    root_dir = os.path.dirname(os.path.abspath(__file__))
    failed_tests = []
    passed_count = 0
    total_count = 0

    print("🚀 Initiating Process-Isolated Enterprise Compliance Audit Suite...\n")

    # Walk through the directory tree
    for root, dirs, files in os.walk(root_dir):
        for file in files:
            if file.startswith('test_') and file.endswith('.py'):
                total_count += 1
                abs_file_path = os.path.join(root, file)
                relative_path = os.path.relpath(abs_file_path, root_dir)
                
                print(f"🔄 Executing: {relative_path}")
                
                # Run the individual test file in its native folder context
                result = subprocess.run(
                    [sys.executable, file],
                    cwd=root,  # This forces Python to treat this folder as the root directory
                    capture_output=True,
                    text=True
                )
                
                if result.returncode == 0:
                    print(f"✅ PASSED: {file}\n")
                    passed_count += 1
                else:
                    print(f"❌ FAILED: {file}")
                    print(f"--- LOG ERROR START ---\n{result.stderr}{result.stdout}\n--- LOG ERROR END ---\n")
                    failed_tests.append(relative_path)

    # Print final execution audit matrix
    print("=" * 60)
    print(f"📊 FINAL AUDIT METRICS: {passed_count}/{total_count} PASSED")
    print("=" * 60)

    if failed_tests:
        print("\n🚨 CRITICAL DEPLOYMENT BLOCK: The following test contexts failed:")
        for current_failed in failed_tests:
            print(f" - {current_failed}")
        sys.exit(1)
    else:
        print("\n🏆 SUCCESS: All micro-services and compliance criteria are 100% compliant.")
        sys.exit(0)

if __name__ == "__main__":
    run_all_compliance_tests()

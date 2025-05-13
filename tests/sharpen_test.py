import subprocess
import sys
import os
from pathlib import Path


def run_config_test(config_path, description):
    """Run the image editing tool with the specified config file."""
    print(f"\n{'=' * 60}")
    print(f"TESTING CONFIGURATION: {description}")
    print(f"Config file: {config_path}")
    print(f"{'=' * 60}")

    # Find the project root directory (parent of tests directory)
    project_root = Path(__file__).parent.parent
    main_path = project_root / "main.py"

    # Make sure we use the full path to the config file
    config_full_path = Path(__file__).parent / config_path

    # Set PYTHONPATH to include the project root for proper imports
    env = os.environ.copy()
    env["PYTHONPATH"] = str(project_root)

    cmd = [sys.executable, str(main_path), "--config", str(config_full_path)]
    result = subprocess.run(cmd, capture_output=True, text=True, env=env)

    # Print output
    if result.stdout:
        print("\nOutput:")
        print(result.stdout)

    # Print any errors
    if result.stderr:
        print("\nErrors:")
        print(result.stderr)

    print(f"Exit code: {result.returncode}")
    return result.returncode == 0


def main():
    """Run tests on different config files to demonstrate operation order effects."""
    # Define the config file paths - use paths relative to the test file
    config1_path = "configs/sharpen.json"

    # Check if config files exist
    test_dir = Path(__file__).parent
    for path in [config1_path]:
        if not (test_dir / path).exists():
            print(f"Error: Config file {path} not found in {test_dir}!")
            return 1

    # Run each test
    success1 = run_config_test(config1_path,
                               "Sharpen filter")

    # Summary
    print("\n" + "=" * 60)
    print("TEST SUMMARY")
    print("=" * 60)
    print(f"Config 1 (Sharpen): {'PASS' if success1 else 'FAIL'}")
    return None


if __name__ == "__main__":
    main()

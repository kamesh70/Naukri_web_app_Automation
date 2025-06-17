import pytest
import webbrowser
import os
import time
import sys


# def main():
#     # Run all tests in the "tests" folder with verbose output and generate a report
#     pytest_args = [
#         "tests",  # Directory where test files are located
#         "-v",  # Verbose mode
#         "--tb=short",  # Short traceback
#         "--html=report.html",  # Generate HTML report
#         "--self-contained-html"  # Ensure the report is standalone
#     ]
#
#     # Run pytest with specified arguments
#     pytest.main(pytest_args)
#
#
#     # Automatically open the generated report
#     report_path = os.path.abspath("report.html")  # Get absolute path
#     webbrowser.open("file://" + report_path)  # Open in default web browser
#
#
#
# if __name__ == "__main__":
#     while True:
#         main()
#         time.sleep(120)  # Wait for 2 minutes before calling again
#




def main(suite_name=None):
    # Base pytest arguments
    pytest_args = [
        "tests",  # Test directory
        "-v",
        "--tb=short",
        "--html=report.html",
        "--self-contained-html"
    ]

    # If a suite is specified, add the marker
    if suite_name and suite_name.lower() != "all":
        pytest_args += ["-m", suite_name]

    # Run pytest with arguments
    pytest.main(pytest_args)

    # Open HTML report
    report_path = os.path.abspath("report.html")
    webbrowser.open("file://" + report_path)


if __name__ == "__main__":
    # Get suite name from command line, default to "all"
    selected_suite = sys.argv[1] if len(sys.argv) > 1 else "all"

    while True:
        main(selected_suite)
        # main("smoke")
        time.sleep(120)  # Repeat every 2 minutes




# def main(suite_name):
#     # Build pytest args based on suite
#     pytest_args = [
#         "tests",  # Directory with test files
#         "-v",
#         "--tb=short",
#         "--html=report.html",
#         "--self-contained-html",
#         "-m", suite_name  # Run only the selected marker
#     ]
#
#     # Run pytest
#     pytest.main(pytest_args)
#
#     # Open the HTML report
#     report_path = os.path.abspath("report.html")
#     webbrowser.open("file://" + report_path)
#
#
# if __name__ == "__main__":
#     # Choose test suite here (or take from command line)
#     selected_suite = "smoke"  # Change to 'sanity' or 'regression' as needed
#
#     while True:
#         main(selected_suite)
#         time.sleep(120)  # Wait for 2 minutes before re-running

# Day 20 - Python Package Manager
# Python packages are reusable code created by other developers.
# pip is Python's package manager. We use pip to install, uninstall,
# upgrade, and list packages.
#
# Important:
# This file does not install packages automatically.
# It teaches the commands and shows safe examples.


import importlib.util
import subprocess
import sys


print("Day 20 - Python Package Manager")
print("=" * 45)


# 1. What is pip?
# pip is used from terminal/PowerShell, not usually inside Python code.
#
# Check pip version:
# python -m pip --version
#
# Why use python -m pip?
# It makes sure pip belongs to the same Python you are running.
print("1. pip is used to manage external Python packages")
print("Command: python -m pip --version")


print("-" * 45)


# 2. Check Python executable
# This tells which Python is running this file.
print("2. Current Python executable")
print(sys.executable)


print("-" * 45)


# 3. Common pip commands
print("3. Common pip commands")
print("Install package:        python -m pip install package_name")
print("Install exact version:  python -m pip install package_name==1.2.3")
print("Upgrade package:        python -m pip install --upgrade package_name")
print("Uninstall package:      python -m pip uninstall package_name")
print("List packages:          python -m pip list")
print("Package details:        python -m pip show package_name")
print("Freeze packages:        python -m pip freeze")


print("-" * 45)


# 4. Example package names
# These are popular packages used in real projects:
popular_packages = {
    "requests": "Call APIs and download web data",
    "pandas": "Work with tables, Excel, and CSV data",
    "numpy": "Work with numbers and arrays",
    "flask": "Create small web applications and APIs",
    "django": "Create large web applications",
    "pytest": "Write and run tests",
    "python-dotenv": "Load settings from .env files",
}

print("4. Popular Python packages")
for package_name, use_case in popular_packages.items():
    print(package_name, ":", use_case)


print("-" * 45)


# 5. Check if a package is installed
# importlib.util.find_spec() checks whether Python can import a package.
def is_package_installed(package_name):
    package = importlib.util.find_spec(package_name)
    return package is not None


package_to_check = "requests"

print("5. Check installed package")
if is_package_installed(package_to_check):
    print(package_to_check, "is installed")
else:
    print(package_to_check, "is not installed")
    print("Install command: python -m pip install", package_to_check)


print("-" * 45)


# 6. Import a package after installing
# Example:
# First install:
# python -m pip install requests
#
# Then use:
# import requests
# response = requests.get("https://example.com")
# print(response.status_code)
print("6. Install first, then import the package in Python")


print("-" * 45)


# 7. requirements.txt
# requirements.txt stores project dependencies.
# This helps another developer install the same packages.
#
# Create requirements.txt:
# python -m pip freeze > requirements.txt
#
# Install from requirements.txt:
# python -m pip install -r requirements.txt
print("7. requirements.txt keeps package list for a project")
print("Create:  python -m pip freeze > requirements.txt")
print("Install: python -m pip install -r requirements.txt")


print("-" * 45)


# 8. Virtual environment
# A virtual environment keeps project packages separate.
# This avoids package conflicts between projects.
#
# Create virtual environment:
# python -m venv .venv
#
# Activate on Windows PowerShell:
# .\\.venv\\Scripts\\Activate.ps1
#
# Deactivate:
# deactivate
print("8. Virtual environment commands")
print("Create:   python -m venv .venv")
print("Activate: .\\.venv\\Scripts\\Activate.ps1")
print("Stop:     deactivate")


print("-" * 45)


# 9. Get pip list using Python
# subprocess lets Python run terminal commands.
# This example is safe because it only lists packages.
print("9. Show first few installed packages")

try:
    result = subprocess.run(
        [sys.executable, "-m", "pip", "list"],
        capture_output=True,
        text=True,
        check=True,
    )

    package_lines = result.stdout.splitlines()

    for line in package_lines[:8]:
        print(line)
except Exception as error:
    print("Could not run pip list:", error)


print("-" * 45)


# 10. Real-world workflow for a new Python project
project_steps = [
    "Create project folder",
    "Create virtual environment using python -m venv .venv",
    "Activate virtual environment",
    "Install required packages using python -m pip install package_name",
    "Write code and import packages",
    "Save dependencies using python -m pip freeze > requirements.txt",
    "Share code with requirements.txt",
]

print("10. Real-world project workflow")
for step_number, step in enumerate(project_steps, start=1):
    print(step_number, "-", step)


print("-" * 45)


# 11. Real-world example: packages for common project types
project_packages = {
    "API project": ["fastapi", "uvicorn", "requests"],
    "Data analysis project": ["pandas", "numpy", "matplotlib"],
    "Web app project": ["django", "python-dotenv"],
    "Testing project": ["pytest"],
}

print("11. Packages by project type")
for project_type, packages in project_packages.items():
    print(project_type, ":", packages)


print("-" * 45)


# 12. Package version
# Sometimes a project needs a specific version.
#
# Install exact version:
# python -m pip install requests==2.31.0
#
# Install minimum version:
# python -m pip install "requests>=2.31.0"
print("12. Package version examples")
print("Exact version:   python -m pip install requests==2.31.0")
print("Minimum version: python -m pip install \"requests>=2.31.0\"")


print("-" * 45)


# 13. Best practices
best_practices = [
    "Use a virtual environment for every project",
    "Use python -m pip instead of only pip",
    "Keep requirements.txt updated",
    "Do not install random packages without checking their purpose",
    "Read package documentation before using it",
    "Use trusted packages with many users when possible",
]

print("13. Best practices")
for practice in best_practices:
    print("-", practice)


print("-" * 45)


# 14. What should you know about package managers?
# - pip installs external packages
# - Packages must be installed before import
# - python -m pip is safer than plain pip
# - requirements.txt stores dependency names and versions
# - virtual environments keep projects separate
# - pip list shows installed packages
# - pip show gives package details
# - pip freeze prints exact installed package versions
# - Use official documentation when learning a package
print("14. Summary completed")

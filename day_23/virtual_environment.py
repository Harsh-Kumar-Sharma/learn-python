# Day 23 - Virtual Environment in Python
# A virtual environment is an isolated Python setup for one project.
# It keeps project packages separate from other projects.
#
# Example:
# Project A can use Django 4
# Project B can use Django 5
# Both projects can work safely because each has its own virtual environment.


import os
import sys


print("Day 23 - Virtual Environment")
print("=" * 50)


# 1. Why do we need a virtual environment?
reasons = [
    "Keep project packages separate",
    "Avoid version conflicts",
    "Make project setup easier for other developers",
    "Keep global Python clean",
    "Use requirements.txt for the same package versions",
]

print("1. Why virtual environment is useful")
for reason in reasons:
    print("-", reason)


print("-" * 50)


# 2. Check current Python executable
# This shows which Python is running this file.
print("2. Current Python executable")
print(sys.executable)


print("-" * 50)


# 3. Check if currently inside a virtual environment
# If sys.prefix is different from sys.base_prefix, a virtual environment is active.
print("3. Check virtual environment status")

if sys.prefix != sys.base_prefix:
    print("Virtual environment is active")
    print("Environment path:", sys.prefix)
else:
    print("Virtual environment is not active")
    print("Base Python path:", sys.base_prefix)


print("-" * 50)


# 4. Create virtual environment
# Run this command in PowerShell from your project folder:
print("4. Create virtual environment")
print("Command:")
print("python -m venv .venv")


print("-" * 50)


# 5. Activate virtual environment on Windows PowerShell
print("5. Activate virtual environment on Windows PowerShell")
print("Command:")
print(".\\.venv\\Scripts\\Activate.ps1")


print("-" * 50)


# 6. Activate virtual environment on Command Prompt
print("6. Activate virtual environment on CMD")
print("Command:")
print(".venv\\Scripts\\activate.bat")


print("-" * 50)


# 7. Activate virtual environment on macOS/Linux
print("7. Activate virtual environment on macOS/Linux")
print("Command:")
print("source .venv/bin/activate")


print("-" * 50)


# 8. Deactivate virtual environment
print("8. Deactivate virtual environment")
print("Command:")
print("deactivate")


print("-" * 50)


# 9. Install packages inside virtual environment
print("9. Install packages after activation")
print("Example commands:")
print("python -m pip install requests")
print("python -m pip install pandas")
print("python -m pip install fastapi uvicorn")


print("-" * 50)


# 10. Save installed packages to requirements.txt
print("10. Save packages")
print("Command:")
print("python -m pip freeze > requirements.txt")


print("-" * 50)


# 11. Install packages from requirements.txt
print("11. Install packages from requirements.txt")
print("Command:")
print("python -m pip install -r requirements.txt")


print("-" * 50)


# 12. Common project structure
project_structure = [
    "my_project/",
    "    .venv/",
    "    main.py",
    "    requirements.txt",
    "    README.md",
]

print("12. Common project structure")
for line in project_structure:
    print(line)


print("-" * 50)


# 13. Real-world workflow
workflow = [
    "Open project folder in terminal",
    "Create environment: python -m venv .venv",
    "Activate environment",
    "Install packages using python -m pip install package_name",
    "Write your Python code",
    "Save package list using python -m pip freeze > requirements.txt",
    "Deactivate when work is done",
]

print("13. Real-world workflow")
for step_number, step in enumerate(workflow, start=1):
    print(step_number, "-", step)


print("-" * 50)


# 14. Check common virtual environment folder names
current_folder = os.getcwd()
possible_env_folders = [".venv", "venv", "env"]

print("14. Check environment folders in current project")
print("Current folder:", current_folder)

for folder_name in possible_env_folders:
    folder_path = os.path.join(current_folder, folder_name)

    if os.path.exists(folder_path):
        print(folder_name, "exists")
    else:
        print(folder_name, "not found")


print("-" * 50)


# 15. Common problems and fixes
problems = {
    "activate script blocked": "Run PowerShell as normal user and use correct activation command",
    "pip not found": "Use python -m pip instead of only pip",
    "package installed but import fails": "Check if virtual environment is activated",
    "wrong Python version": "Check python --version and sys.executable",
    "requirements install fails": "Check package name, version, and internet connection",
}

print("15. Common problems and fixes")
for problem, fix in problems.items():
    print(problem, "->", fix)


print("-" * 50)


# 16. Best practices
best_practices = [
    "Create one virtual environment per project",
    "Name it .venv or venv",
    "Do not upload .venv folder to GitHub",
    "Upload requirements.txt",
    "Use python -m pip for package commands",
    "Activate environment before running project code",
    "Keep requirements.txt updated",
]

print("16. Best practices")
for practice in best_practices:
    print("-", practice)


print("-" * 50)


# 17. What should you know about virtual environments?
# - A virtual environment isolates project packages
# - Create it using python -m venv .venv
# - Activate it before installing packages
# - Use deactivate to exit it
# - requirements.txt stores package versions
# - Do not commit .venv folder to GitHub
# - Use sys.executable to check which Python is running
# - Use sys.prefix and sys.base_prefix to check if venv is active
print("17. Summary completed")

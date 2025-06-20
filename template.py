# Importing required modules
import os  # For directory and file operations
from pathlib import Path  # For OS-independent file path handling
import logging  # For logging events and debugging

# Configuring the logging format and level
logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s:')

# Setting the project name
project_name = "cnnClassifier"

# List of files and folders to be created
list_of_files = [
    ".github/workflows/.gitkeep",  # Hidden GitHub folder (for CI/CD workflows)
    f"src/{project_name}/__init__.py",  # Marks this directory as a Python package
    f"src/{project_name}/components/__init__.py",  # Components folder
    f"src/{project_name}/utils/__init__.py",  # Utilities folder
    f"src/{project_name}/config/__init__.py",  # Configuration folder
    f"src/{project_name}/config/configuration.py",  # Main config file
    f"src/{project_name}/pipeline/__init__.py",  # Pipeline logic
    f"src/{project_name}/entity/__init__.py",  # Data entity definitions
    f"src/{project_name}/constants/__init__.py",  # Constants used across project
    "config/config.yaml",  # YAML file for global configuration
    "dvc.yaml",  # DVC pipeline file
    "params.yaml",  # Hyperparameters
    "requirements.txt",  # Python dependencies
    "setup.py",  # Python package setup script
    "research/trials.ipynb",  # Jupyter notebook for experiments
    "templates/index.html"  # HTML template (possibly for UI)
]

# Loop through each file path
for filepath in list_of_files:
    filepath = Path(filepath)  # Convert string path to Path object  and this will returns as you are in windows or linux
    filedir, filename = os.path.split(filepath)  # Split into directory and file name

    # If directory part is not empty, create it (if it doesn’t exist)
    if filedir != "":
        os.makedirs(filedir, exist_ok=True)  # Create directory
        logging.info(f"Creating directory; {filedir} for the file: {filename}")

    # If the file does not exist or is empty, create an empty file
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, "w") as f:
            pass  # Creates an empty file
        logging.info(f"Creating empty file: {filepath}")
    else:
        # If file already exists and is not empty
        logging.info(f"{filename} is already exists")

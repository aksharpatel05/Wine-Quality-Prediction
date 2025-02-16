import os  # Provides functions to interact with the operating system
from pathlib import Path  # A more convenient way to handle file paths
import logging  # Handles logging messages

#logging module to display logs at the INFO level
logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s:')

#define the project name
project_name="Wine_Quality_Prediction"

#creating list of files and directories
list_of_files=[
    ".github/workflows/.gitkeep",
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/utils/common.py",
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/config/configuration.py",
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/entity/config_entity.py",
    f"src/{project_name}/constants/__init__.py",
    "config/config.yaml",
    "params.yaml",
    "schema.yaml",
    "main.py",
    "Dockerfile",
    "setup.py",
    "research/research.ipynb",
    "templates/index.html",
    "app.py"
]


#Creating Files and Directories
for filepath in list_of_files:
    filepath=Path(filepath)  # Convert to a Path object
    filedir, filename = os.path.split(filepath)  # Separate directory and filename

    if filedir != "":
        os.makedirs(filedir, exist_ok=True)  # Create directories if they don't exist
        logging.info(f"Creating directory {filedir} for the file : {filename}")


#Creating Empty Files If Not Exists
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, "w") as f:  # Create an empty file
            pass
        logging.info(f"Creating empty file: {filepath}")
    #Handling Existing Files
    else:
        logging.info(f"{filename} already exists")

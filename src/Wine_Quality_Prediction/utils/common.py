import os
import yaml
from src.Wine_Quality_Prediction import logger  # Custom logger for logging
import json
import joblib
from ensure import ensure_annotations  # Ensures function annotations are followed
from box import ConfigBox  # Converts dictionaries into objects with dot-access attributes
from pathlib import Path  # Provides an object-oriented interface for filesystem paths
from typing import Any  # Allows specifying generic types
from box.exceptions import BoxValueError  # Exception handling for ConfigBox

#reading YAML file
@ensure_annotations
def read_yaml(path_to_yaml: Path) -> ConfigBox:
    """Reads a YAML file and returns its contents as a ConfigBox object.

    Args:
        path_to_yaml (Path): Path to the YAML file.

    Raises:
        ValueError: If the YAML file is empty.
        e: If an unexpected error occurs.

    Returns:
        ConfigBox: Data from the YAML file with dot notation access.
    """
    try:
        with open(path_to_yaml) as yaml_file:
            content = yaml.safe_load(yaml_file)  # Load YAML safely
            logger.info(f"YAML file: {path_to_yaml} loaded successfully")
            return ConfigBox(content)  # Converts dict to dot-accessible object
    except BoxValueError:
        raise ValueError("YAML file is empty")  # Raises an error if the file is empty
    except Exception as e:
        raise e  # Rethrows any other unexpected errors

#Creating Directories
@ensure_annotations
def create_directories(path_to_directories: list, verbose=True):
    """Creates multiple directories.

    Args:
        path_to_directories (list): List of directories to create.
        verbose (bool): If True, logs the directory creation.
    """
    for path in path_to_directories:
        os.makedirs(path, exist_ok=True)  # Creates the directory if it doesn’t exist
        if verbose:
            logger.info(f"Created directory at: {path}")

#Saving and Loading JSON Files
@ensure_annotations
def save_json(path: Path, data: dict):
    """Saves a dictionary as a JSON file.

    Args:
        path (Path): Path to the JSON file.
        data (dict): Data to be saved.
    """
    with open(path, "w") as f:
        json.dump(data, f, indent=4)  # Pretty-print JSON with indentation
    logger.info(f"JSON file saved at: {path}")

@ensure_annotations
def load_json(path: Path) -> ConfigBox:
    """Loads data from a JSON file.

    Args:
        path (Path): Path to the JSON file.

    Returns:
        ConfigBox: Data as class attributes instead of a dictionary.
    """
    with open(path) as f:
        content = json.load(f)  # Load JSON file
    logger.info(f"JSON file loaded successfully from: {path}")
    return ConfigBox(content)  # Returns data with dot-access

#Saving and Loading Binary Files
@ensure_annotations
def save_bin(data: Any, path: Path):
    """Saves data as a binary file using joblib.

    Args:
        data (Any): Data to be saved.
        path (Path): Path to the binary file.
    """
    joblib.dump(value=data, filename=path)  # Save binary file
    logger.info(f"Binary file saved at: {path}")

@ensure_annotations
def load_bin(path: Path) -> Any:
    """Loads binary data from a file.

    Args:
        path (Path): Path to the binary file.

    Returns:
        Any: The object stored in the file.
    """
    data = joblib.load(path)  # Load binary file
    logger.info(f"Binary file loaded from: {path}")
    return data


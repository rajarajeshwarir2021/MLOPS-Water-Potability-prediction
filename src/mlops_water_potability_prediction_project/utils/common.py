import os
from box.exceptions import BoxValueError
import yaml
from src.mlops_water_potability_prediction_project import logger
import json
import joblib
from ensure import ensure_annotations
from box import ConfigBox
from pathlib import Path
from typing import Any


@ensure_annotations
def read_yaml(path_to_yaml: Path) -> ConfigBox:
    """
    Reads a YAML file from the given path and returns a ConfigBox.

    Args:
        path_to_yaml: path to the YAML file
    Returns:
        ConfigBox: ConfigBox
    Raises:
        ValueError: if the yaml file is empty
        e: empty yaml file
    """
    try:
        with open(path_to_yaml) as yaml_file:
            content = yaml.safe_load(yaml_file)
            logger.info(f"YAML file: {path_to_yaml} loaded successfully")
            return ConfigBox(content)
    except BoxValueError:
        raise ValueError("YAML file is empty")
    except Exception as e:
        raise e


@ensure_annotations
def create_directories(directories_path_list: list, verbose=True) -> None:
    """
    Create directories given a list of directories.

    Args:
        directories_path_list: list of directory paths to create
        verbose: to log the status, default True
    Returns: None
    """
    for path in directories_path_list:
        os.makedirs(path, exist_ok=True)
        if verbose:
            logger.info(f"Created directory at: {path}")


@ensure_annotations
def save_json(file_path: Path, data: dict, verbose: True) -> None:
    """
    Save a JSON file.

    Args:
        file_path: path to save the json file
        data: a dictionary to save
        verbose: to log the status, default True
    Returns: None
    """
    with open(file_path, 'w') as f:
        json.dump(data, f, indent=4)
    if verbose:
        logger.info(f"JSON file saved at: {file_path}")


@ensure_annotations
def load_json(file_path: Path, verbose: True) -> ConfigBox:
    """
    Load a JSON file.

    Args:
        file_path: path to load the json file from
        verbose: to log the status, default True
    Returns:
        ConfigBox: file content
    """
    with open(file_path) as f:
        content = json.load(f)
    if verbose:
        logger.info(f"JSON file loaded from: {file_path}")
    return ConfigBox(content)


@ensure_annotations
def save_binary(data: Any, file_path: Path, verbose=True) -> None:
    """
    Save data as a binary file.

    Args:
        data: data to save
        file_path: path to save the binary file
        verbose: to log the status, default True
    Returns: None
    """
    joblib.dump(value=data, filename=file_path)
    if verbose:
        logger.info(f"Binary file saved at: {file_path}")


@ensure_annotations
def load_binary(file_path: Path, verbose: True) -> Any:
    """
    Load a Binary file.

    Args:
        file_path: path to load the binary file from
        verbose: to log the status, default True
    Returns:
        Any: file content
    """
    content = joblib.load(file_path)
    if verbose:
        logger.info(f"Binary file loaded from: {file_path}")
    return content


@ensure_annotations
def get_size(file_path: Path) -> str:
    """
    Get the file size in KB.

    Args:
        file_path: path to the file
    Returns:
        str: file size in KB
    """
    size_kb = round(os.path.getsize(file_path)/1024, 2)
    size_str = f"{size_kb} KB"
    return size_str
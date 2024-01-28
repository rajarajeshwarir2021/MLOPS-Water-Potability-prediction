from box import ConfigBox
from box.exceptions import BoxValueError
from ensure import ensure_annotations
import os
from pathlib import Path
from typing import Any
import yaml

from src.mlops_water_potability_prediction_project import logger
from src.mlops_water_potability_prediction_project.classes.dataloadersaver import JobLibDataLoaderSaver, \
    JSONDataLoaderSaver


@ensure_annotations
def create_directories(directories_path_list: list, verbose=True):
    """
    Create directories given a list of directories.

    Args:
        directories_path_list (list): List of directory paths to create
        verbose (bool): To log the status, default True
    Returns: None
    """
    for path in directories_path_list:
        try:
            os.makedirs(path, exist_ok=True)
            if verbose:
                logger.info(f"Created directory at: {path}")
        except Exception as e:
            if verbose:
                logger.error(f"Error creating directory at {path}: {e}")


@ensure_annotations
def get_file_size(file_path: Path) -> str:
    """
    Get the file size in KB.

    Args:
        file_path (Path): Path to the file
    Returns:
        str: File size in KB
    """
    size_kb = round(os.path.getsize(file_path)/1024, 2)
    size_str = f"{size_kb} KB"
    return size_str


@ensure_annotations
def load_binary(file_path: Path, verbose: True) -> Any:
    """
    Load a Binary file.

    Args:
        file_path (Path): Path to load the binary file from
        verbose (bool): To log the status, default True
    Returns:
        Any: File content or None
    """
    try:
        content = JobLibDataLoaderSaver.load(file_path)
        if verbose:
            logger.info(f"Binary file loaded from: {file_path}")
        return content
    except Exception as e:
        if verbose:
            logger.error(f"Error loading binary file from {file_path}: {e}")
        return None


@ensure_annotations
def save_binary(file_path: Path, data: Any, verbose=True) -> None:
    """
    Save data as a binary file.

    Args:
        file_path (Path): Path to save the binary file
        data (Any): Data to save
        verbose (bool): To log the status, default True
    Returns:
        None
    """
    try:
        JobLibDataLoaderSaver.save(file_path, data)
        if verbose:
            logger.info(f"Binary file saved at: {file_path}")
    except Exception as e:
        if verbose:
            logger.error(f"Error saving binary file at {file_path}: {e}")


@ensure_annotations
def load_json(file_path: Path, verbose: True) -> Any:
    """
    Load a JSON file.

    Args:
        file_path (Path): Path to load the JSON file from
        verbose (bool): To log the status, default True
    Returns:
        Any: File content ConfigBox or None
    """
    try:
        content = JSONDataLoaderSaver.load(file_path)
        if verbose:
            logger.info(f"JSON file loaded from: {file_path}")
        return ConfigBox(content)
    except Exception as e:
        if verbose:
            logger.error(f"Error loading JSON file from {file_path}: {e}")
        return None


@ensure_annotations
def save_json(file_path: Path, data: dict, verbose: True) -> None:
    """
    Save a JSON file.

    Args:
        file_path (Path): Path to save the JSON file
        data (dict): A dictionary to save
        verbose (bool): To log the status, default True
    Returns:
        None
    """
    try:
        JSONDataLoaderSaver.save(file_path, data)
        if verbose:
            logger.info(f"JSON file saved at: {file_path}")
    except Exception as e:
        if verbose:
            logger.error(f"Error saving JSON file at {file_path}: {e}")


@ensure_annotations
def read_yaml(path_to_yaml: Path) -> ConfigBox:
    """
    Reads a YAML file from the given path and returns a ConfigBox.

    Args:
        path_to_yaml (Path): Path to the YAML file
    Returns:
        ConfigBox (ConfigBox): File content ConfigBox
    Raises:
        ValueError: If the yaml file is empty
        e: Empty yaml file
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





















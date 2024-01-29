import json
from abc import ABC, abstractmethod
from pathlib import Path
from typing import Any

import joblib


class DataLoaderSaver(ABC):
    """
    An abstract class to load and save data.
    """
    @abstractmethod
    def load(self, file_path: Path) -> Any:
        """
        An abstract method to load from the given file path.

        Args:
            file_path: path to the file to load
        Returns:
            Any: object
        """
        pass

    @abstractmethod
    def save(self, file_path: Path, data: Any) -> None:
        """
        An abstract method to save data to the given file path.

        Args:
            file_path: path to the file to load
            data: object to save
        Returns:
            None
        """
        pass


class JSONDataLoaderSaver(DataLoaderSaver):
    """
    A class to load and save JSON data.
    """
    def load(self, file_path: Path) -> Any:
        """
        A method to load from the given file path.

        Args:
            file_path: path to the json file to load
        Returns:
            Any: object
        """
        try:
            with open(file_path) as f:
                content = json.load(f)
            return content
        except FileNotFoundError:
            print(f"File not found: {file_path}")
            return None
        except Exception as e:
            print(f"An error occurred: {e}")
            return None

    def save(self, file_path: Path, data: dict) -> None:
        """
        A method to save data to the given file path.

        Args:
            file_path: path to the json file to load
            data: object to save
        Returns:
            None
        """
        try:
            with open(file_path, 'w') as f:
                json.dump(data, f, indent=4)
        except Exception as e:
            print(f"An error occurred while saving data: {e}")


class JobLibDataLoaderSaver(DataLoaderSaver):
    """
    A class to load and save Binary data.
    """

    def load(self, file_path: Path) -> Any:
        """
        A method to load from the given file path.

        Args:
            file_path: path to the joblib file to load
        Returns:
            Any: object
        """
        try:
            content = joblib.load(file_path)
            return content
        except FileNotFoundError:
            print(f"File not found: {file_path}")
            return None
        except Exception as e:
            print(f"An error occurred: {e}")
            return None

    def save(self, file_path: Path, data: Any) -> None:
        """
        A method to save data to the given file path.

        Args:
            file_path: path to the joblib file to load
            data: object to save
        Returns:
            None
        """
        try:
            joblib.dump(value=data, filename=file_path)
        except Exception as e:
            print(f"An error occurred while saving data: {e}")
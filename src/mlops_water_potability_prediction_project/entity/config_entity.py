from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True)
class DataIngestionConfig:
    """
    Configuration class for data ingestion.

    Attributes:
    - source_url (str): The URL from which data will be ingested.
    - root_dir (Path): The root directory where data will be stored.
    - unzip_dir (Path): The directory where ingested data will be unzipped.
    - zip_data_path (Path): The path where zipped data will be stored.
    """
    source_url: str
    root_dir: Path
    unzip_dir: Path
    zip_data_path: Path


@dataclass(frozen=True)
class DataValidationConfig:
    """
    Configuration class for data validation.

    Attributes:
    - root_dir (Path): The root directory where data validation will be performed.
    - unzip_data_path (Path): The path where unzipped data will be stored for validation.
    - status_file (str): The file containing status information of the validation process.
    - data_schema (dict): A dictionary representing the expected schema for the validation data.
    """
    root_dir: Path
    data_path: Path
    status_file: str
    data_schema: dict


@dataclass(frozen=True)
class DataTransformationConfig:
    """
    Configuration class for data transformation.

    Attributes:
        - root_dir (Path): The root directory for data transformation.
        - data_path (Path): The path to the data for transformation.
        - status_file (str): The file containing status information of the validation process.
    """
    root_dir: Path
    data_path: Path
    status_file: Path
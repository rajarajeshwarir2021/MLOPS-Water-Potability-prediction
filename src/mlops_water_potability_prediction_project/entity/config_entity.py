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
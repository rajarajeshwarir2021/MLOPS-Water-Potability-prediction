import os
from pathlib import Path
import urllib.request as request
import zipfile

from src.mlops_water_potability_prediction_project import logger
from src.mlops_water_potability_prediction_project.entity.config_entity import DataIngestionConfig
from src.mlops_water_potability_prediction_project.utilities.helpers import get_file_size


class DataIngestion:
    """
    A class for handling the data ingestion process.

    Attributes:
    - config (DataIngestionConfig): The configuration for data ingestion.

    Methods:
    - __init__: Initializes a DataIngestion instance with the provided configuration.
    - download_file: Downloads the data file from the specified source URL to the configured path.
    - extract_zip_file: Extracts the contents of the downloaded zip file to the specified directory.
    """

    def __init__(self, config: DataIngestionConfig):
        """
        Initializes a DataIngestion instance with the provided configuration.

        Parameters:
        - config (DataIngestionConfig): The configuration for data ingestion.
        """
        self.config = config

    def download_file(self):
        """
        Downloads the data file from the specified source URL to the configured path.
        If the file already exists, logs its size; otherwise, logs the successful download.

        Returns:
        - None
        """
        try:
            if not os.path.exists(self.config.zip_data_path):
                filename, headers = request.urlretrieve(
                    url=self.config.source_url,
                    filename=self.config.zip_data_path
                )
                logger.info(f"{filename} download! \nWith the following info: \n{headers}")
            else:
                logger.info(f"File already exists. Size: {get_file_size(Path(self.config.zip_data_path))}")
        except Exception as e:
            logger.error(f"Error during file download: {e}")

    def extract_zip_file(self):
        """
        Extracts the contents of the downloaded zip file to the specified directory.

        Returns:
        - None
        """
        try:
            unzip_path = self.config.unzip_dir
            os.makedirs(unzip_path, exist_ok=True)
            with zipfile.ZipFile(self.config.zip_data_path, 'r') as zip_ref:
                zip_ref.extractall(unzip_path)
        except Exception as e:
            logger.error(f"Error during zip file extraction: {e}")

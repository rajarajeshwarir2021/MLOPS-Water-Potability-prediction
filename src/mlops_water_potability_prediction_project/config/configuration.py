from src.mlops_water_potability_prediction_project.constants import *
from src.mlops_water_potability_prediction_project.entity.config_entity import DataIngestionConfig
from src.mlops_water_potability_prediction_project.utilities.helpers import read_yaml, create_directories


class ConfigurationManager:
    """
    A class for managing configuration settings related to data ingestion.

    Attributes:
    - config_filepath [Path]: The filepath for the main configuration file.
    - params_filepath [Path]: The filepath for the parameters file.
    - schema_filepath [Path]: The filepath for the schema file.

    Methods:
    - __init__: Initializes the ConfigurationManager instance with default or provided filepaths,
                reads YAML files, and creates necessary directories.
    - get_data_ingestion_config: Retrieves the data ingestion configuration from the main configuration.
    """
    def __init__(self, config_filepath=CONFIG_FILE_PATH, params_filepath=PARAMS_FILE_PATH, schema_filepath=SCHEMA_FILE_PATH):
        """
        Initializes a ConfigurationManager instance.

        Parameters:
        - config_filepath [Path]: The filepath for the main configuration file.
        - params_filepath [Path]: The filepath for the parameters file.
        - schema_filepath [Path]: The filepath for the schema file.
        """
        self.config = read_yaml(config_filepath)
        self.params = read_yaml(params_filepath)
        self.schema = read_yaml(schema_filepath)

        create_directories(directories_path_list=[self.config.artifacts_root])

    def get_data_ingestion_config(self) -> DataIngestionConfig:
        """
        Retrieves the data ingestion configuration from the main configuration.

        Returns:
        - DataIngestionConfig: An instance of DataIngestionConfig with the specified configuration.
        """
        config = self.config.data_ingestion

        create_directories([config.root_dir])

        data_ingestion_config = DataIngestionConfig(
            source_url=config.source_url,
            root_dir=config.root_dir,
            unzip_dir=config.unzip_dir,
            zip_data_path=config.zip_data_path
        )

        return data_ingestion_config
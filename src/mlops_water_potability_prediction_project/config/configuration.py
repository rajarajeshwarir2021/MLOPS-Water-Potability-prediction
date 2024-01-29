from src.mlops_water_potability_prediction_project.constants import *
from src.mlops_water_potability_prediction_project.entity.config_entity import DataIngestionConfig, \
    DataValidationConfig, DataTransformationConfig, DataCleaningConfig
from src.mlops_water_potability_prediction_project.utilities.helpers import read_yaml, create_directories


class ConfigurationManager:
    """
    A class for retrieving data ingestion, data validation, data transformation configuration.

    Attributes:
    - config_filepath [Path]: The filepath for the main configuration file.
    - params_filepath [Path]: The filepath for the parameters file.
    - schema_filepath [Path]: The filepath for the schema file.

    Methods:
    - __init__: Initializes the ConfigurationManager instance with default or provided filepaths,
                reads YAML files, and creates necessary directories.
    - get_data_ingestion_config: Retrieves the data ingestion configuration from the main configuration.
    - get_data_validation_config: Retrieves the data validation configuration from the main configuration.
    - get_data_transformation_config: Retrieves data transformation configuration from the main configuration.
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

    def get_data_cleaning_config(self) -> DataCleaningConfig:
        """
        Retrieve the data cleaning configuration.

        Returns:
        - DataCleaningConfig: An instance of DataCleaningConfig containing the configuration settings.

        Notes:
            The method uses the data cleaning configuration from the overall application configuration.
            It creates the necessary directories specified in the configuration.
        """
        config = self.config.data_cleaning

        # Ensure the root directory exists
        create_directories([config.root_dir])

        # Create and return a DataCleaningConfig instance
        data_cleaning_config = DataCleaningConfig(
            root_dir=config.root_dir,
            unclean_data_path=config.unclean_data_path,
            clean_data_path=config.clean_data_path
        )

        return data_cleaning_config

    def get_data_validation_config(self) -> DataValidationConfig:
        """
        Retrieves the data validation configuration from the main configuration.

        Returns:
        - DataValidationConfig: An instance of DataValidationConfig with the specified configuration.
        """
        config = self.config.data_validation
        schema = self.schema.COLUMNS

        create_directories([config.root_dir])

        data_validation_config = DataValidationConfig(
            root_dir=config.root_dir,
            data_path=config.data_path,
            status_file=config.status_file,
            data_schema=schema
        )

        return data_validation_config

    def get_data_transformation_config(self) -> DataTransformationConfig:
        """
        Retrieves the data transformation configuration.

        Returns:
        - DataTransformationConfig: An instance of DataTransformationConfig based on the stored configuration data.
        """
        config = self.config.data_transformation

        create_directories([config.root_dir])

        data_transformation_config = DataTransformationConfig(
            root_dir=config.root_dir,
            data_path=config.data_path,
            status_file=config.status_file,
            feature_scaler=config.feature_scaler
        )

        return data_transformation_config


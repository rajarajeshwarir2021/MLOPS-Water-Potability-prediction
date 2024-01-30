import os.path

import pandas as pd
from src.mlops_water_potability_prediction_project import logger
from src.mlops_water_potability_prediction_project.entity.config_entity import DataCleaningConfig


class DataCleaning:
    """
    DataCleaning class for cleaning data.

    Attributes:
        config (DataCleaningConfig): The configuration for data cleaning.

    Methods:
        clean_data(): Reads unclean data, removes any rows with missing values, and saves the cleaned data.

    Note:
        This class assumes the use of a logger instance from the 'src.mlops_water_potability_prediction_project' module.
    """

    def __init__(self, config: DataCleaningConfig):
        """
        Initialize DataCleaning instance.

        Args:
            config (DataCleaningConfig): The configuration for data cleaning.
        """
        self.config = config

    def clean_data(self):
        """
        Clean the data by removing rows with missing values.

        Raises:
            Exception: If an error occurs during the cleaning process.
        """
        try:
            # Read the unclean data
            dataframe = pd.read_csv(self.config.unclean_data_path)

            # Remove rows with any missing values
            dataframe = dataframe.dropna(how='any', axis=0)

            # Save the cleaned data
            dataframe.to_csv(self.config.clean_data_path, index=False)

            # Save the cleaned data schema
            overview = dataframe.describe()
            overview.loc[["min", "max"]].to_json(os.path.join(self.config.root_dir, "dataset_schema.json"))

            # Log information about the cleaning process
            logger.info("Cleaned the dataset")

        except Exception as e:
            # Raise an exception if an error occurs during cleaning
            raise e
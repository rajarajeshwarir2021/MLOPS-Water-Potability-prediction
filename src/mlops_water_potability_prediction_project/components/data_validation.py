import pandas as pd

from src.mlops_water_potability_prediction_project import logger
from src.mlops_water_potability_prediction_project.entity.config_entity import DataValidationConfig


class DataValidation:
    """
    A class for performing data validation based on specified configuration.

    Attributes:
    - config (DataValidationConfig): The configuration for data validation.

    Methods:
    - __init__: Initializes a DataValidation instance with the provided configuration.
    - validate_all_columns: Validates all columns in the dataset against the specified data schema.
    """

    def __init__(self, config: DataValidationConfig):
        """
        Initializes a DataValidation instance with the provided configuration.

        Parameters:
        - config (DataValidationConfig): The configuration for data validation.
        """
        self.config = config

    def validate_all_columns(self) -> bool:
        """
        Validates all columns in the dataset against the specified data schema.

        Returns:
        - bool: True if all columns pass validation, False otherwise.
        """
        try:
            validation_status = None
            dataframe = pd.read_csv(self.config.data_path)
            all_columns = list(dataframe.columns)
            data_schema_keys = self.config.data_schema.keys()

            for col in all_columns:
                if col not in data_schema_keys:
                    validation_status = False
                elif dataframe[col].dtype != self.config.data_schema[col]:
                    validation_status = False
                else:
                    continue

            if validation_status == None:
                validation_status = True

            with open(self.config.status_file, 'w') as f:
                f.write(f"Validation status: {str(validation_status)}")

            logger.info(f"Validation status: {str(validation_status)}")
            return validation_status
        except Exception as e:
            logger.error(f"Error during data validation: {e}")
            raise e
from src.mlops_water_potability_prediction_project import logger
from src.mlops_water_potability_prediction_project.components.data_validation import DataValidation
from src.mlops_water_potability_prediction_project.config.configuration import ConfigurationManager

STAGE_NAME = "DATA VALIDATION"


class DataValidationTrainingPipeline:
    """
    A class representing a data validation training pipeline.

    Methods:
    - __init__: Initializes a DataValidationTrainingPipeline instance.
    - validate_data: Executes the validation steps of the data validation training pipeline.
    """

    def __init__(self):
        """
        Initializes a DataValidationTrainingPipeline instance.
        """
        pass

    def validate_data(self):
        """
        Executes the validation steps of the data validation training pipeline.
        Retrieves configuration, performs data validation, and logs errors if any.

        Returns:
        - None
        """
        try:
            config = ConfigurationManager()
            data_validation_config = config.get_data_validation_config()
            data_validation = DataValidation(config=data_validation_config)
            data_validation.validate_all_columns()
        except Exception as e:
            logger.error(f"Error during data validation training pipeline: {e}")
            raise e



if __name__ == '__main__':
    try:
        logger.info(f">>>>>> STAGE: {STAGE_NAME} started <<<<<<")
        DataValidationTrainingPipeline().validate_data()
        logger.info(f">>>>>> STAGE: {STAGE_NAME} completed <<<<<<\n\nX==========X")
    except Exception as e:
        logger.error(f"Error during overall execution: {e}")
        raise e
from src.mlops_water_potability_prediction_project import logger
from src.mlops_water_potability_prediction_project.components.data_cleaning import DataCleaning
from src.mlops_water_potability_prediction_project.config.configuration import ConfigurationManager

STAGE_NAME = "DATA CLEANING"


class DataCleaningTrainingPipeline:
    """
    DataCleaningTrainingPipeline class for orchestrating the data cleaning process in the training pipeline.

    Methods:
        clean_data(): Initiates the data cleaning process using the configuration and DataCleaning class.

    Note:
        This class assumes the use of a logger instance from the 'src.mlops_water_potability_prediction_project' module.
    """

    def __init__(self):
        """
        Initialize DataCleaningTrainingPipeline instance.
        """
        pass

    def clean_data(self):
        """
        Clean the data as part of the training pipeline.

        Raises:
            Exception: If an error occurs during the data cleaning process.
        """
        try:
            # Retrieve the data cleaning configuration
            config = ConfigurationManager()
            data_cleaning_config = config.get_data_cleaning_config()

            # Create a DataCleaning instance with the retrieved configuration
            data_cleaning = DataCleaning(config=data_cleaning_config)

            # Initiate the data cleaning process
            data_cleaning.clean_data()

        except Exception as e:
            logger.error(f"Error during data cleaning training pipeline: {e}")
            raise e


if __name__ == '__main__':
    try:
        logger.info(f">>>>>> STAGE: {STAGE_NAME} started <<<<<<")
        DataCleaningTrainingPipeline().clean_data()
        logger.info(f">>>>>> STAGE: {STAGE_NAME} completed <<<<<<\n\nX==========X")
    except Exception as e:
        logger.error(f"Error during overall execution: {e}")
        raise e
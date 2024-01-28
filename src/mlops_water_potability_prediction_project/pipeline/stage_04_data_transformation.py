from pathlib import Path

from src.mlops_water_potability_prediction_project import logger
from src.mlops_water_potability_prediction_project.components.data_transformation import DataTransformation
from src.mlops_water_potability_prediction_project.config.configuration import ConfigurationManager
from src.mlops_water_potability_prediction_project.entity.config_entity import DataTransformationConfig

STAGE_NAME = "DATA TRANSFORMATION"


class DataTransformationTrainingPipeline:
    """
    A class representing a data transformation training pipeline.

    Methods:
    - __init__: Initializes a DataTransformationTrainingPipeline instance.
    - transform_data: Executes the main steps of the data transformation training pipeline.
    - validate_data: Validates the data schema by checking the status in status.txt file.
    """

    def __init__(self):
        """
        Initializes a DataTransformationTrainingPipeline instance.
        """
        pass

    def transform_data(self):
        """
        Executes the transformation steps of the data transformation training pipeline.

        Returns:
        - None
        """
        try:
            config = ConfigurationManager()
            data_transformation_config: DataTransformationConfig = config.get_data_transformation_config()
            status_file_path = data_transformation_config.status_file

            if DataTransformationTrainingPipeline.validate_data(status_file_path):
                data_transformation = DataTransformation(config=data_transformation_config)
                data_transformation.split_dataset()
                data_transformation.feature_scale_dataset()
                data_transformation.save_transformation()
            else:
                logger.error("Invalid Data schema")
                raise Exception("Invalid Data schema")
        except Exception as e:
            logger.error(f"Error during data transformation training pipeline: {e}")
            raise e

    @staticmethod
    def validate_data(status_file_path):
        """
        Validates the data schema by checking the status in status.txt file.

        Returns:
        - bool: True if the data schema is valid, False otherwise.
        """
        try:
            with open(Path(status_file_path), 'r') as f:
                status = f.read().split(" ")[-1]
            if status == "True":
                return True
            else:
                return False
        except Exception as e:
            logger.error(f"Error while trying to read status.txt: {e}")
            raise e


if __name__ == '__main__':
    try:
        logger.info(f">>>>>> STAGE: {STAGE_NAME} started <<<<<<")
        DataTransformationTrainingPipeline().transform_data()
        logger.info(f">>>>>> STAGE: {STAGE_NAME} completed <<<<<<\n\nX==========X")
    except Exception as e:
        logger.error(f"Error during overall execution: {e}")
        raise e
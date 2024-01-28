from src.mlops_water_potability_prediction_project import logger
from src.mlops_water_potability_prediction_project.components.data_ingestion import DataIngestion
from src.mlops_water_potability_prediction_project.config.configuration import ConfigurationManager

STAGE_NAME = "DATA INGESTION"


class DataIngestionTrainingPipeline:
    """
    A class representing a data ingestion training pipeline.

    Methods:
    - __init__: Initializes a DataIngestionTrainingPipeline instance.
    - main: Executes the main steps of the data ingestion training pipeline.
    """

    def __init__(self):
        """
        Initializes a DataIngestionTrainingPipeline instance.
        """
        pass

    def main(self):
        """
        Executes the main steps of the data ingestion training pipeline.
        Retrieves configuration, performs data ingestion, downloads and extracts the zipfile.

        Returns:
        - None
        """
        try:
            config = ConfigurationManager()
            data_ingestion_config = config.get_data_ingestion_config()
            data_ingestion = DataIngestion(config=data_ingestion_config)
            data_ingestion.download_file()
            data_ingestion.extract_zip_file()
        except Exception as e:
            logger.error(f"Error during data ingestion training pipeline: {e}")
            raise e



if __name__ == '__main__':
    try:
        logger.info(f">>>>>> STAGE: {STAGE_NAME} started <<<<<<")
        DataIngestionTrainingPipeline().main()
        logger.info(f">>>>>> STAGE: {STAGE_NAME} completed <<<<<<\n\nX==========X")
    except Exception as e:
        logger.error(f"Error during overall execution: {e}")
        raise e
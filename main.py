from src.mlops_water_potability_prediction_project import logger
from src.mlops_water_potability_prediction_project.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline

STAGE_NAME = "DATA INGESTION"


try:
    logger.info(f">>>>>> STAGE: {STAGE_NAME} started <<<<<<")
    DataIngestionTrainingPipeline().main()
    logger.info(f">>>>>> STAGE: {STAGE_NAME} completed <<<<<<\n\nX==========X")
except Exception as e:
    logger.error(f"Error during overall execution: {e}")
    raise e
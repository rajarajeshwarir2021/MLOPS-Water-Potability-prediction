from src.mlops_water_potability_prediction_project import logger
from src.mlops_water_potability_prediction_project.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from src.mlops_water_potability_prediction_project.pipeline.stage_03_data_validation import \
    DataValidationTrainingPipeline
from src.mlops_water_potability_prediction_project.pipeline.stage_04_data_transformation import \
    DataTransformationTrainingPipeline

# STAGE_NAME = "DATA INGESTION"
# try:
#     logger.info(f">>>>>> STAGE: {STAGE_NAME} started <<<<<<")
#     DataIngestionTrainingPipeline().ingest_data()
#     logger.info(f">>>>>> STAGE: {STAGE_NAME} completed <<<<<<\n\nX==========X")
# except Exception as e:
#     logger.error(f"Error during overall execution: {e}")
#     raise e


STAGE_NAME = "DATA VALIDATION"
try:
    logger.info(f">>>>>> STAGE: {STAGE_NAME} started <<<<<<")
    DataValidationTrainingPipeline().validate_data()
    logger.info(f">>>>>> STAGE: {STAGE_NAME} completed <<<<<<\n\nX==========X")
except Exception as e:
    logger.error(f"Error during overall execution: {e}")
    raise e

STAGE_NAME = "DATA TRANSFORMATION"
if __name__ == '__main__':
    try:
        logger.info(f">>>>>> STAGE: {STAGE_NAME} started <<<<<<")
        DataTransformationTrainingPipeline().transform_data()
        logger.info(f">>>>>> STAGE: {STAGE_NAME} completed <<<<<<\n\nX==========X")
    except Exception as e:
        logger.error(f"Error during overall execution: {e}")
        raise e
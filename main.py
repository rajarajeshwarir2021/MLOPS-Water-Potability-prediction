from src.mlops_water_potability_prediction_project import logger
from src.mlops_water_potability_prediction_project.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from src.mlops_water_potability_prediction_project.pipeline.stage_02_data_cleaning import DataCleaningTrainingPipeline
from src.mlops_water_potability_prediction_project.pipeline.stage_03_data_validation import \
    DataValidationTrainingPipeline
from src.mlops_water_potability_prediction_project.pipeline.stage_04_data_transformation import \
    DataTransformationTrainingPipeline
from src.mlops_water_potability_prediction_project.pipeline.stage_05_model_trainer import ModelTrainerTrainingPipeline
from src.mlops_water_potability_prediction_project.pipeline.stage_06_model_evaluation import \
    ModelEvaluationTrainingPipeline
from src.mlops_water_potability_prediction_project.pipeline.stage_07_model_prediction import ModelPredictionPipeline


SAMPLE_DATA = [[-0.3178266699547379,-0.091211066334705,-0.8620216614125349,-0.6109023585675367,-0.45494327621466607,-1.0186105292775014,0.9252077219311549,-0.8142465077043499,-1.5108829669361032]]
def main():
    """
    The main function runs different stages of the training pipeline
    Returns: None
    """

    STAGE_NAME = "DATA INGESTION"
    try:
        logger.info(f">>>>>> STAGE: {STAGE_NAME} started <<<<<<")
        DataIngestionTrainingPipeline().ingest_data()
        logger.info(f">>>>>> STAGE: {STAGE_NAME} completed <<<<<<\n\nX==========X")
    except Exception as e:
        logger.error(f"Error during overall execution: {e}")
        raise e

    STAGE_NAME = "DATA CLEANING"
    try:
        logger.info(f">>>>>> STAGE: {STAGE_NAME} started <<<<<<")
        DataCleaningTrainingPipeline().clean_data()
        logger.info(f">>>>>> STAGE: {STAGE_NAME} completed <<<<<<\n\nX==========X")
    except Exception as e:
        logger.error(f"Error during overall execution: {e}")
        raise e

    STAGE_NAME = "DATA VALIDATION"
    try:
        logger.info(f">>>>>> STAGE: {STAGE_NAME} started <<<<<<")
        DataValidationTrainingPipeline().validate_data()
        logger.info(f">>>>>> STAGE: {STAGE_NAME} completed <<<<<<\n\nX==========X")
    except Exception as e:
        logger.error(f"Error during overall execution: {e}")
        raise e

    STAGE_NAME = "DATA TRANSFORMATION"
    try:
        logger.info(f">>>>>> STAGE: {STAGE_NAME} started <<<<<<")
        DataTransformationTrainingPipeline().transform_data()
        logger.info(f">>>>>> STAGE: {STAGE_NAME} completed <<<<<<\n\nX==========X")
    except Exception as e:
        logger.error(f"Error during overall execution: {e}")
        raise e

    STAGE_NAME = "MODEL TRAINER"
    try:
        logger.info(f">>>>>> STAGE: {STAGE_NAME} started <<<<<<")
        ModelTrainerTrainingPipeline().train_model()
        logger.info(f">>>>>> STAGE: {STAGE_NAME} completed <<<<<<\n\nX==========X")
    except Exception as e:
        logger.error(f"Error during overall execution: {e}")
        raise e

    STAGE_NAME = "MODEL EVALUATION"
    try:
        logger.info(f">>>>>> STAGE: {STAGE_NAME} started <<<<<<")
        ModelEvaluationTrainingPipeline().evaluate_model()
        logger.info(f">>>>>> STAGE: {STAGE_NAME} completed <<<<<<\n\nX==========X")
    except Exception as e:
        logger.error(f"Error during overall execution: {e}")
        raise e

    STAGE_NAME = "MODEL PREDICTION"
    try:
        logger.info(f">>>>>> STAGE: {STAGE_NAME} started <<<<<<")
        ModelPredictionPipeline().predict_model(SAMPLE_DATA)
        logger.info(f">>>>>> STAGE: {STAGE_NAME} completed <<<<<<\n\nX==========X")
    except Exception as e:
        logger.error(f"Error during overall execution: {e}")
        raise e


if __name__ == '__main__':
    main()

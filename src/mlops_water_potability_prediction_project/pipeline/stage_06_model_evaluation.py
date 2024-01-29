from src.mlops_water_potability_prediction_project import logger
from src.mlops_water_potability_prediction_project.components.model_evaluation import ModelEvaluation
from src.mlops_water_potability_prediction_project.config.configuration import ConfigurationManager

STAGE_NAME = "MODEL EVALUATION"


class ModelEvaluationTrainingPipeline:
    """
    ModelEvaluationTrainingPipeline class for orchestrating the model evaluation process in the training pipeline.

    Methods:
        evaluate_model(): Initiates the model evaluation process using the configuration and ModelEvaluation class.

    Note:
        This class assumes the use of a logger instance from the 'src.mlops_water_potability_prediction_project' module.
    """

    def __init__(self):
        """
        Initialize ModelEvaluationTrainingPipeline instance.
        """
        pass

    def evaluate_model(self):
        """
        Evaluate the model as part of the training pipeline.

        Raises:
            Exception: If an error occurs during the model evaluation process.
        """
        try:
            # Retrieve the model evaluation configuration
            config = ConfigurationManager()
            model_evaluation_config = config.get_model_evaluation_config()

            # Create a ModelEvaluation instance with the retrieved configuration
            model_evaluation = ModelEvaluation(config=model_evaluation_config)

            # Initiate the model evaluation process
            model_evaluation.evaluate()

        except Exception as e:
            # Log an error message and raise an exception if an error occurs
            logger.error(f"Error during model evaluation training pipeline: {e}")
            raise e


if __name__ == '__main__':
    try:
        logger.info(f">>>>>> STAGE: {STAGE_NAME} started <<<<<<")
        ModelEvaluationTrainingPipeline().evaluate_model()
        logger.info(f">>>>>> STAGE: {STAGE_NAME} completed <<<<<<\n\nX==========X")
    except Exception as e:
        logger.error(f"Error during overall execution: {e}")
        raise e
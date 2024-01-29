from src.mlops_water_potability_prediction_project import logger
from src.mlops_water_potability_prediction_project.components.model_trainer import ModelTrainer
from src.mlops_water_potability_prediction_project.config.configuration import ConfigurationManager

STAGE_NAME = "MODEL TRAINER"


class ModelTrainerTrainingPipeline:
    """
    ModelTrainerTrainingPipeline class for orchestrating the model training process in the training pipeline.

    Methods:
        train_model(): Initiates the model training process using the configuration and ModelTrainer class.

    Note:
        This class assumes the use of a logger instance from the 'src.mlops_water_potability_prediction_project' module.
    """

    def __init__(self):
        """
        Initialize ModelTrainerTrainingPipeline instance.
        """
        pass

    def train_model(self):
        """
        Train the model as part of the training pipeline.

        Raises:
            Exception: If an error occurs during the model training process.
        """
        try:
            # Retrieve the model trainer configuration
            config = ConfigurationManager()
            model_trainer_config = config.get_model_trainer_config()

            # Create a ModelTrainer instance with the retrieved configuration
            model_trainer = ModelTrainer(config=model_trainer_config)

            # Initiate the model training process
            model_trainer.train()

        except Exception as e:
            # Log an error message and raise an exception if an error occurs
            logger.error(f"Error during model training training pipeline: {e}")
            raise e


if __name__ == '__main__':
    try:
        logger.info(f">>>>>> STAGE: {STAGE_NAME} started <<<<<<")
        ModelTrainerTrainingPipeline().train_model()
        logger.info(f">>>>>> STAGE: {STAGE_NAME} completed <<<<<<\n\nX==========X")
    except Exception as e:
        logger.error(f"Error during overall execution: {e}")
        raise e
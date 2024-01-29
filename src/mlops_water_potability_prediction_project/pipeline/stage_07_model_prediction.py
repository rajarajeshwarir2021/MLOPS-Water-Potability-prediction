from src.mlops_water_potability_prediction_project import logger
from src.mlops_water_potability_prediction_project.components.model_prediction import ModelPrediction
from src.mlops_water_potability_prediction_project.config.configuration import ConfigurationManager

STAGE_NAME = "MODEL PREDICTION"


class ModelPredictionPipeline:
    """
    ModelPredictionPipeline class for orchestrating the model prediction process.

    Methods:
        predict_model(): Initiates the model prediction process using the configuration and ModelPrediction class.

    Note:
        This class assumes the use of a logger instance from the 'src.mlops_water_potability_prediction_project' module.
    """

    def __init__(self):
        """
        Initialize ModelPredictionPipeline instance.
        """
        pass

    def predict_model(self, data):
        """
        Predict using the model as part of the prediction pipeline.

        Args:
            data: The input data for making predictions.

        Raises:
            Exception: If an error occurs during the model prediction process.
        """
        try:
            # Retrieve the model prediction configuration
            config = ConfigurationManager()
            model_prediction_config = config.get_model_prediction_config()

            # Create a ModelPrediction instance with the retrieved configuration
            model_prediction = ModelPrediction(config=model_prediction_config)

            # Initiate the model prediction process
            prediction = model_prediction.predict(data)
            print(prediction)

        except Exception as e:
            # Log an error message and raise an exception if an error occurs
            logger.error(f"Error during model prediction pipeline: {e}")
            raise e


if __name__ == '__main__':
    try:
        logger.info(f">>>>>> STAGE: {STAGE_NAME} started <<<<<<")
        ModelPredictionPipeline().evaluate_model()
        logger.info(f">>>>>> STAGE: {STAGE_NAME} completed <<<<<<\n\nX==========X")
    except Exception as e:
        logger.error(f"Error during overall execution: {e}")
        raise e
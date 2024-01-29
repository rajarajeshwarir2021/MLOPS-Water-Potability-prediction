import joblib
from src.mlops_water_potability_prediction_project import logger
from src.mlops_water_potability_prediction_project.entity.config_entity import ModelPredictionConfig


class ModelPrediction:
    """
    ModelPrediction class for making predictions using a trained model.

    Attributes:
        config (ModelPredictionConfig): The configuration for model prediction.

    Methods:
        predict(data): Makes predictions using the provided data and the trained model.

    Note:
        This class assumes the use of a logger instance from the 'src.mlops_water_potability_prediction_project' module.
    """

    def __init__(self, config: ModelPredictionConfig):
        """
        Initialize ModelPrediction instance.

        Args:
            config (ModelPredictionConfig): The configuration for model prediction.
        """
        self.config = config

    def predict(self, data):
        """
        Make predictions using the trained model.

        Args:
            data: The input data for making predictions.

        Returns:
            The predictions made by the model.

        Raises:
            Exception: If an error occurs during the prediction process.
        """
        try:
            # Load the trained model
            model = joblib.load(self.config.model_path)

            # Make predictions using the model
            prediction = model.predict(data)

            # Log information about the prediction process
            logger.info("Predict data using the model")

            return prediction

        except Exception as e:
            # Raise an exception if an error occurs during prediction
            raise e
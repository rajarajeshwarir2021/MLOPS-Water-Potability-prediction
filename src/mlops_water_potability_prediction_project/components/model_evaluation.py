import joblib
import mlflow
import mlflow.sklearn
import numpy as np
import os
import pandas as pd
from pathlib import Path
from sklearn.metrics import accuracy_score, confusion_matrix
from urllib.parse import urlparse

from src.mlops_water_potability_prediction_project import logger
from src.mlops_water_potability_prediction_project.entity.config_entity import ModelEvaluationConfig
from src.mlops_water_potability_prediction_project.utilities.helpers import save_json

os.environ["MLFLOW_TRACKING_URI"]="https://dagshub.com/rajarajeshwarir2021/MLOPS-Water-Potability-prediction.mlflow"
os.environ["MLFLOW_TRACKING_USERNAME"]="rajarajeshwarir2021"
os.environ["MLFLOW_TRACKING_PASSWORD"]="9bcd728f7628e9db2e294588d97d9589df5ea9b1"


class ModelEvaluation:
    """
    ModelEvaluation class for evaluating a machine learning model.

    Attributes:
        config (ModelEvaluationConfig): The configuration for model evaluation.

    Methods:
        evaluate(): Evaluates the model using the provided configuration and logs metrics with MLflow.

    Note:
        This class assumes the use of a logger instance from the 'src.mlops_water_potability_prediction_project' module.
    """

    def __init__(self, config: ModelEvaluationConfig):
        """
        Initialize ModelEvaluation instance.

        Args:
            config (ModelEvaluationConfig): The configuration for model evaluation.
        """
        self.config = config

    def evaluate(self):
        """
        Evaluate the model and log metrics with MLflow.

        Raises:
            Exception: If an error occurs during the evaluation process.
        """
        try:
            # Read testing data and load the model
            test_df = pd.read_csv(self.config.test_data_path)
            model = joblib.load(self.config.model_path)

            # Extract features and target variables
            X_test = test_df.drop([self.config.target_column], axis=1)
            y_test = test_df[[self.config.target_column]]

            # Configure Dagshub and MLflow tracking
            mlflow.set_registry_uri(self.config.mlflow_uri)
            tracking_url_type_store = urlparse(mlflow.get_tracking_uri()).scheme

            # Start an MLflow run
            with mlflow.start_run():
                # Make predictions using the model
                y_pred = model.predict(X_test)

                # Evaluate metrics
                accuracy, conf_matrix = ModelEvaluation.evaluate_metrics(y_test, y_pred)

                # Save metrics locally
                score = {
                    "Accuracy": accuracy,
                    "True_Positive": int(conf_matrix[0][0]),
                    "True_Negative": int(conf_matrix[1][1]),
                    "False_Positive": int(conf_matrix[0][1]),
                    "False_Negative": int(conf_matrix[1][0])
                }
                metric_file_path = Path(os.path.join(self.config.root_dir, self.config.metric_file_name))
                save_json(metric_file_path, score)

                # Log parameters and metrics with MLflow
                mlflow.log_param("Iteration", self.config.parameters.iterations)
                mlflow.log_param("Learning_rate", self.config.parameters.learning_rate)
                mlflow.log_param("Random_seed", self.config.parameters.random_seed)
                mlflow.log_metric("Accuracy", accuracy)
                mlflow.log_metric("True_Positive", int(conf_matrix[0][0]))
                mlflow.log_metric("True_Negative", int(conf_matrix[1][1]))
                mlflow.log_metric("False_Positive", int(conf_matrix[0][1]))
                mlflow.log_metric("False_Negative", int(conf_matrix[1][0]))

            # Log the model with MLflow
            if tracking_url_type_store != "file":
                mlflow.sklearn.log_model(model, "model", registered_model_name="CatBoostModel")
            else:
                mlflow.sklearn.log_model(model, "model", registered_model_name="CatBoostModel")

            logger.info("Evaluated and logged metrics with MLflow")

        except Exception as e:
            # Raise an exception if an error occurs during evaluation
            raise e

    @staticmethod
    def evaluate_metrics(actual: np.ndarray, predict: np.ndarray):
        """
        Evaluate metrics such as accuracy and confusion matrix.

        Args:
            actual: The actual target values.
            predict: The predicted target values.

        Returns:
            Tuple[float, np.ndarray]: A tuple containing accuracy and confusion matrix.
        """
        accuracy = round(accuracy_score(actual, predict), 2)
        conf_matrix = confusion_matrix(actual, predict)
        return accuracy, conf_matrix

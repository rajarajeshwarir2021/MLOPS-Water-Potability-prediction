import joblib
import os
import pandas as pd
from catboost import CatBoostClassifier
from src.mlops_water_potability_prediction_project import logger

class ModelTrainer:
    """
    ModelTrainer class for training a CatBoostClassifier.

    Attributes:
        config (ModelTrainerConfig): The configuration for model training.

    Methods:
        train(): Reads training and testing data, trains a CatBoostClassifier, and saves the trained model.

    Note:
        This class assumes the use of a logger instance from the 'src.mlops_water_potability_prediction_project' module.
    """

    def __init__(self, config: ModelTrainerConfig):
        """
        Initialize ModelTrainer instance.

        Args:
            config (ModelTrainerConfig): The configuration for model training.
        """
        self.config = config

    def train(self):
        """
        Train a CatBoostClassifier using the provided configuration.

        Raises:
            Exception: If an error occurs during the training process.
        """
        try:
            # Read training and testing data
            train_df = pd.read_csv(self.config.train_data_path)
            test_df = pd.read_csv(self.config.test_data_path)

            # Extract features and target variables
            X_train = train_df.drop([self.config.target_column], axis=1)
            X_test = test_df.drop([self.config.target_column], axis=1)
            y_train = train_df[[self.config.target_column]]
            y_test = test_df[[self.config.target_column]]

            # Initialize and train CatBoostClassifier
            classifier = CatBoostClassifier(iterations=self.config.iterations,
                                            random_seed=self.config.random_seed,
                                            learning_rate=self.config.learning_rate,
                                            custom_loss=self.config.custom_loss)
            classifier.fit(X_train, y_train, verbose=True, plot=True)

            # Save the trained model
            model_path = os.path.join(self.config.root_dir, self.config.model_file_name)
            joblib.dump(classifier, model_path)

            # Log information about the training process
            logger.info("Trained and saved the model")

        except Exception as e:
            # Raise an exception if an error occurs during training
            raise e
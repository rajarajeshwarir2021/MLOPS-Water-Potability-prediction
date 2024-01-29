import os

import joblib
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

from src.mlops_water_potability_prediction_project import logger
from src.mlops_water_potability_prediction_project.entity.config_entity import DataTransformationConfig


class DataTransformation:
    """
    A class for performing data transformation operations.

    Attributes:
    - config (DataTransformationConfig): The configuration for data transformation.
    - train (pd.DataFrame): The training set after data transformation.
    - test (pd.DataFrame): The test set after data transformation.

    Methods:
    - __init__: Initializes a DataTransformation instance with the provided configuration.
    - split_dataset: Splits the dataset into training and test sets.
    - feature_scale_dataset: Applies feature scaling to the datasets.
    - save_transformation: Saves the transformed datasets as CSV files.
    """

    def __init__(self, config: DataTransformationConfig):
        """
        Initializes a DataTransformation instance with the provided configuration.

        Parameters:
        - config (DataTransformationConfig): The configuration for data transformation.
        """
        self.config = config
        self.train = None
        self.test = None

    def split_dataset(self):
        """
        Splits the dataset into training and test sets.

        Returns:
        - None
        """
        try:
            dataframe = pd.read_csv(self.config.data_path)

            self.train, self.test = train_test_split(dataframe)

            logger.info("Split the dataset into train and test sets")
            logger.info(f"Train set shape: {self.train.shape}")
            logger.info(f"Test set shape: {self.test.shape}")

        except Exception as e:
            raise e

    def feature_scale_dataset(self):
        """
        Applies feature scaling to the datasets.

        Returns:
        - None
        """
        try:
            sc = StandardScaler()

            train_array = self.train.to_numpy()
            test_array = self.test.to_numpy()

            train_array[:, :-1] = sc.fit_transform(train_array[:, :-1])
            test_array[:, :-1] = sc.transform(test_array[:, :-1])

            self.train = pd.DataFrame(train_array, columns=list(self.train.columns))
            self.test = pd.DataFrame(test_array, columns=list(self.test.columns))

            logger.info("Feature scaled the train and test sets")

            joblib.dump(sc, os.path.join(self.config.root_dir, self.config.feature_scaler))
            logger.info("Saved the Feature scaler")

        except Exception as e:
            raise e

    def save_transformation(self):
        """
        Saves the transformed datasets as CSV files.

        Returns:
        - None
        """
        try:
            self.train.to_csv(os.path.join(self.config.root_dir, "train_set.csv"), index=False)
            self.test.to_csv(os.path.join(self.config.root_dir, "test_set.csv"), index=False)

            logger.info("Saved the transformations as csv")
        except Exception as e:
            raise e
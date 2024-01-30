import joblib
import json
import numpy as np
import pandas as pd
from src.mlops_water_potability_prediction_project import logger
from src.mlops_water_potability_prediction_project.entity.config_entity import ModelFrontendConfig


class NotInRange(Exception):
    def __init__(self, message="Values entered are not in range"):
        self.message = message
        super().__init__(self.message)


class NotInFeatureColumn(Exception):
    def __init__(self, message="Values entered are not in feature columns"):
        self.message = message
        super().__init__(self.message)


class FrontendPrediction:
    """
    A class for making predictions using a machine learning model in the frontend.

    Attributes:
    - config (ModelFrontendConfig): The configuration for the model frontend.

    Methods:
    - __init__: Initializes a FrontendPrediction instance with the provided configuration.
    - form_response: Forms a response based on the prediction result.
    - model_predict: Makes predictions using the loaded machine learning model.
    - validate_input: Validates the input data against the dataset schema.
    - feature_scale: Applies feature scaling to the input data.
    - get_schema: Retrieves the dataset schema from a specified path.
    - create_dataframe: Creates a Pandas DataFrame from a dictionary of input data.
    """

    def __init__(self, config: ModelFrontendConfig):
        """
        Initializes a FrontendPrediction instance with the provided configuration.

        Parameters:
        - config (ModelFrontendConfig): The configuration for the model frontend.
        """
        self.config = config

    def form_response(self, dict_request):
        """
        Forms a response based on the prediction result.

        Parameters:
        - dict_request (dict): The input data for making predictions.

        Returns:
        - str: The response indicating whether the water is "Potable" or "Not Potable".
        """
        if self.validate_input(dict_request):
            scaled_data = self.feature_scale(dict_request)
            prediction_result = self.model_predict(scaled_data)
            if prediction_result == 1:
                response = "Potable"
            else:
                response = "Not Potable"
            return response

    def model_predict(self, data):
        """
        Makes predictions using the loaded machine learning model.

        Parameters:
        - data (numpy.ndarray): The input data for making predictions.

        Returns:
        - int: The prediction result (0 or 1).
        """
        try:
            model = joblib.load(self.config.model_path)
            prediction = model.predict(data)[0]
            if 0 <= prediction <= 1:
                return prediction
            else:
                raise NotInRange
            logger.info("Predict data using model")
            return prediction
        except Exception as e:
            raise e

    def validate_input(self, data):
        """
        Validates the input data against the dataset schema.

        Parameters:
        - data (dict): The input data for making predictions.

        Returns:
        - bool: True if the input data is valid, False otherwise.
        """

        def _validate_cols(col):
            schema = FrontendPrediction.get_schema(self.config.dataset_schema)
            actual_cols = schema.keys()
            if col not in actual_cols:
                raise NotInFeatureColumn

        def _validate_values(col, val):
            schema = FrontendPrediction.get_schema(self.config.dataset_schema)
            if not (schema[col]["min"] <= float(val) <= schema[col]["max"]):
                raise NotInRange

        for col, val in data.items():
            _validate_cols(col)
            _validate_values(col, val)

        return True

    def feature_scale(self, data):
        """
        Applies feature scaling to the input data.

        Parameters:
        - data (dict): The input data for making predictions.

        Returns:
        - numpy.ndarray: The scaled input data.
        """
        df = FrontendPrediction.create_dataframe(data)
        sc = joblib.load(self.config.feature_scaler)
        data = sc.transform(df)
        return data

    @staticmethod
    def get_schema(schema_path):
        """
        Retrieves the dataset schema from a specified path.

        Parameters:
        - schema_path (str): The path to the dataset schema file.

        Returns:
        - dict: The dataset schema.
        """
        with open(schema_path, 'r') as f:
            schema = json.load(f)
        return schema

    @staticmethod
    def create_dataframe(dict):
        """
        Creates a Pandas DataFrame from a dictionary of input data.

        Parameters:
        - dict (dict): The input data for making predictions.

        Returns:
        - pandas.DataFrame: The created DataFrame.
        """
        data = np.array([list(dict.values())])
        headers = list(dict.keys())
        df = pd.DataFrame(data, columns=headers)
        return df
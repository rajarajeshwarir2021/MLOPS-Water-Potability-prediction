from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True)
class DataIngestionConfig:
    """
    Configuration class for data ingestion.

    Attributes:
    - source_url (str): The URL from which data will be ingested.
    - root_dir (Path): The root directory where data will be stored.
    - unzip_dir (Path): The directory where ingested data will be unzipped.
    - zip_data_path (Path): The path where zipped data will be stored.

    Note:
        This class is decorated with @dataclass, making instances immutable (frozen).
        Immutable instances are useful for configuration settings to prevent accidental modification.
    """
    source_url: str
    root_dir: Path
    unzip_dir: Path
    zip_data_path: Path


@dataclass(frozen=True)
class DataCleaningConfig:
    """
    Configuration class for data cleaning.

    Attributes:
    - root_dir (Path): The root directory where the data is located.
    - unclean_data_path (Path): The path to the unclean/raw data file.
    - clean_data_path (Path): The path where the cleaned data will be saved.

    Note:
        This class is decorated with @dataclass, making instances immutable (frozen).
        Immutable instances are useful for configuration settings to prevent accidental modification.
    """

    root_dir: Path
    unclean_data_path: Path
    clean_data_path: Path


@dataclass(frozen=True)
class DataValidationConfig:
    """
    Configuration class for data validation.

    Attributes:
    - root_dir (Path): The root directory where data validation will be performed.
    - unzip_data_path (Path): The path where unzipped data will be stored for validation.
    - status_file (str): The file containing status information of the validation process.
    - data_schema (dict): A dictionary representing the expected schema for the validation data.

    Note:
        This class is decorated with @dataclass, making instances immutable (frozen).
        Immutable instances are useful for configuration settings to prevent accidental modification.
    """
    root_dir: Path
    data_path: Path
    status_file: str
    data_schema: dict


@dataclass(frozen=True)
class DataTransformationConfig:
    """
    Configuration class for data transformation.

    Attributes:
    - root_dir (Path): The root directory for data transformation.
    - data_path (Path): The path to the data for transformation.
    - status_file (str): The file containing status information of the validation process.

    Note:
        This class is decorated with @dataclass, making instances immutable (frozen).
        Immutable instances are useful for configuration settings to prevent accidental modification.
    """
    root_dir: Path
    data_path: Path
    status_file: Path
    feature_scaler: Path


@dataclass(frozen=True)
class ModelTrainerConfig:
    """
    Configuration class for model training.

    Attributes:
    - root_dir (Path): The root directory where the model training data is located.
    - train_data_path (Path): The path to the training data file.
    - test_data_path (Path): The path to the testing data file.
    - model_file_name (str): The name of the file to save the trained model.
    - iterations (int): The number of iterations for model training.
    - learning_rate (float): The learning rate for the model training.
    - random_seed (int): The random seed for reproducibility.
    - custom_loss (list): A list of custom loss functions to be used during training.
    - target_column (str): The name of the target column in the dataset.

    Note:
        This class is decorated with @dataclass, making instances immutable (frozen).
        Immutable instances are useful for configuration settings to prevent accidental modification.
    """
    root_dir: Path
    train_data_path: Path
    model_file_name: str
    iterations: int
    learning_rate: float
    random_seed: int
    custom_loss: list
    target_column: str


@dataclass(frozen=True)
class ModelEvaluationConfig:
    """
    Configuration class for model evaluation.

    Attributes:
    - root_dir (Path): The root directory where the model evaluation data is located.
    - test_data_path (Path): The path to the testing data file.
    - model_path (Path): The path to the trained model file.
    - metric_file_name (str): The name of the file to save the evaluation metrics.
    - parameters (dict): Additional parameters for model evaluation.
    - target_column (str): The name of the target column in the dataset.
    - mlflow_uri (str): The URI for MLflow tracking (optional).

    Note:
        This class is decorated with @dataclass, making instances immutable (frozen).
        Immutable instances are useful for configuration settings to prevent accidental modification.
    """
    root_dir: Path
    test_data_path: Path
    model_path: Path
    metric_file_name: str
    parameters: dict
    target_column: str
    mlflow_uri: str

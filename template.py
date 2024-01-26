import os
import logging
from pathlib import Path

PROJECT_NAME = "mlops_water_potability_prediction_project"
FILES_TO_GENERATE = [
    ".github/workflows/.gitkeep",
    f"src/{PROJECT_NAME}/__init__.py",
    f"src/{PROJECT_NAME}/classes/__init__.py",
    f"src/{PROJECT_NAME}/step/__init__.py",
    f"src/{PROJECT_NAME}/utils/__init__.py",
    f"src/{PROJECT_NAME}/utils/common.py",
    f"src/{PROJECT_NAME}/config/__init__.py",
    f"src/{PROJECT_NAME}/config/configuration.py",
    f"src/{PROJECT_NAME}/pipeline/__init__.py",
    f"src/{PROJECT_NAME}/entity/__init__.py",
    f"src/{PROJECT_NAME}/entity/config_entity.py",
    f"src/{PROJECT_NAME}/constants/__init__.py",
    "config/config.yaml",
    "dvc.yaml",
    "params.yaml",
    "schema.yaml",
    "main.py",
    "app.py",
    "Dockerfile",
    "requirements.txt",
    "setup.py",
    "notebooks/initial_data_exploration.ipynb",
    "notebooks/exploratory_data_analysis.ipynb",
    "notebooks/data_preprocessing.ipynb",
    "web_app/static/css/main.css",
    "web_app/static/js/main.js",
    "web_app/template/base.html",
    "web_app/template/index.html",
    "web_app/template/error.html",
    "tests/__init__.py",
    "tests/conftest.py",
    "tests/test_config.py"
]

logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s)')


def run_template(template_list: list) -> None:
    """
    A function to create project structure folders and files as provided in the list.
    :param template_list: a list containing the paths to folder and files.
    :return: None
    """
    for file_path in template_list:
        file_path = Path(file_path)
        file_dir, file_name = os.path.split(file_path)

        if file_dir !="":
            os.makedirs(file_dir, exist_ok=True)
            logging.info(f"Creating directory: {file_dir} for the  file: {file_name}")

        if (not os.path.exists(file_path)) or (os.path.getsize(file_path) == 0):
            with open(file_path, 'w') as f:
                pass
                logging.info(f"Creating an empty file: {file_path}")

        else:
            logging.info(f"{file_name} already exists")


if __name__ == '__main__':
    run_template(FILES_TO_GENERATE)

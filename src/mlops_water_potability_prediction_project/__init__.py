import os
import sys
import logging

LOG_DIRECTORY = "logs"
LOGGING_STRING = "[%(asctime)s]: %(levelname)s: %(module)s: %(message)s]"

LOG_FILE_PATH = os.path.join(LOG_DIRECTORY,"run_logs.log")
os.makedirs(LOG_DIRECTORY, exist_ok=True)


logging.basicConfig(
    level=logging.INFO,
    format=LOGGING_STRING,
    handlers=[
        logging.FileHandler(LOG_FILE_PATH),
        logging.StreamHandler(sys.stdout)
    ]
)

logger = logging.getLogger("mlops_water_potability_prediction_project_logger")
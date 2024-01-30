import os

from flask import Flask, render_template, request, jsonify

from src.mlops_water_potability_prediction_project.components.frontend import FrontendPrediction
from src.mlops_water_potability_prediction_project.config.configuration import ConfigurationManager

# Assuming 'data' is a dictionary containing input values
SAMPLE_DATA = {
    'ph': '2',
    'Hardness': '75',
    'Solids': '350',
    'Chloramines': '2',
    'Sulfate': '150',
    'Conductivity': '250',
    'Organic_carbon': '10',
    'Trihalomethanes': '10',
    'Turbidity': '5'
}

# Create a configuration manager instance
config = ConfigurationManager()
frontend_config = config.get_frontend_config()

static_dir = frontend_config.static_dir
templates_dir = frontend_config.template_dir

app = Flask(__name__, static_folder=static_dir, template_folder=templates_dir)


@app.route('/', methods=['GET', 'POST'])
def index():
    """
    Handles requests to the main page.

    If the request method is POST, it attempts to make a prediction using the submitted form data.
    If successful, the prediction result is rendered on the 'index.html' page.
    If there is an error, an error message is rendered on the 'error.html' page.

    If the request method is GET, renders the 'index.html' page.

    Returns:
    - str: Rendered HTML content.
    """
    if request.method == 'POST':
        try:
            if request.form:
                data_req = dict(request.form)
                frontend_predictor = FrontendPrediction(config=frontend_config)
                response = frontend_predictor.form_response(data_req)
                print(response)
                return render_template('index.html', response=response)
        except Exception as e:
            print(e)
            error_message = {"error": e}
            return render_template('error.html', error=error_message)
    else:
        return render_template('index.html')


@app.route('/train', methods=['GET'])
def train_model():
    """
    Handles requests to trigger the model training process.

    Executes the 'main.py' script to train the machine learning model.

    Returns:
    - str: A message indicating the success of the training process.
    """
    os.system("python main.py")
    return "Training Successful!"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
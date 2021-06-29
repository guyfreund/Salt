import logging
from flask import Flask, request, jsonify

from database import Database
from validator import Validator
from constants import ABNORMAL, ABNORMALITIES, SAMPLE_ROUTE, MODEL_ROUTE, PATH

app = Flask("salt")

database = Database(db_root_path="")
validator = Validator(database)


@app.route('/')
def handle_frontpage():
    return 'GFR Salt Project'


@app.route(SAMPLE_ROUTE, methods=['POST'])
def handle_sample():
    sample_data = request.json
    logging.debug(f'Service debug {sample_data}')

    valid, abnormalities = validator.validate(sample_data)
    response = {ABNORMAL: not valid}
    if abnormalities:
        response[ABNORMALITIES] = abnormalities

    return jsonify(response)


@app.route(MODEL_ROUTE, methods=['POST'])
def handle_model():
    model_data = request.json
    logging.debug(f'Service debug {model_data}')
    database.add_model(model_data)

    return f'Added new model of path {model_data[PATH]}'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)

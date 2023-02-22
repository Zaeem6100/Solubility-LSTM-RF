from flask import Flask, request
import logging

app = Flask(__name__)

logger = logging.getLogger('Verifier')
logger.setLevel("DEBUG")


@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'


@app.route('/singleSequence', methods=['GET'])
def singleSequence():
    return 'Hello World!'


@app.route('/multipleSequence', methods=['GET'])
def multipleSequence():
    if request.method != 'POST':
        return "Not Allowed", 405
    return 'Hello World!'


# @app.route('/singleSequence/<string:sequence>', methods=['GET'])
# def singleSequence(sequence):
#     return sequence


@app.errorhandler(404)
def not_found():
    return "Not Found", 404


if __name__ == '__main__':
    app.run()

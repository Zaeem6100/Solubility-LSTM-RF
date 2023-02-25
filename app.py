from flask import Flask, request, render_template

from helper import Predictor

app = Flask(__name__)

app.FLASK_DEBUG = 1


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/singleSequence', methods=['GET'])
def singleSequence():
    return 'Hello World!'


@app.route('/results', methods=['post'])
def results():
    sequences = request.form['sequences']
    pred = Predictor()
    seq = "MGSVRKASAWLGLVDDNDDERYYDDDYAEGQESGEAWVTDPRVKVASETAEEKGRRIGTVTPDSFRDARGIGELFRDGVPVIINLTAMEPTDAKRVVDFAAGLTFGLRGTIERVATRVFLLTPANTEIVSGEAAGRPTDGFFNQS"
    clf = pred.RFInit()
    data = clf.predict(pred.LSTMPredict(sequences.upper()))
    return render_template('results.html', sequences=data[0])


# @app.route('/singleSequence/<string:sequence>', methods=['GET'])
# def singleSequence(sequence):
#     return sequence


@app.errorhandler(404)
def not_found():
    return "Not Found"


if __name__ == '__main__':
    app.run(debug=True)
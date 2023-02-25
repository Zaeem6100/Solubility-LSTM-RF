from flask import Flask, request, render_template

from helper import Predictor

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/results', methods=['post'])
def results():
    sequences = request.form['sequence']
    pred = Predictor()
    seq = "MGSVRKASAWLGLVDDNDDERYYDDDYAEGQESGEAWVTDPRVKVASETAEEKGRRIGTVTPDSFRDARGIGELFRDGVPVIINLTAMEPTDAKRVVDFAAGLTFGLRGTIERVATRVFLLTPANTEIVSGEAAGRPTDGFFNQS"
    clf = pred.RFInit()
    data = clf.predict(pred.LSTMPredict(sequences.upper()))
    print(data[0])
    send = ""
    if data[0] == 1:
        send = "Protein is Soluble"
    else:
        send = "Protein is Insoluble"
    return render_template('index.html', sequences=send, input=sequences.upper())


# @app.route('/singleSequence/<string:sequence>', methods=['GET'])
# def singleSequence(sequence):
#     return sequence


@app.errorhandler(404)
def not_found(error):
    return "Not Found", 404


if __name__ == '__main__':
    app.run()
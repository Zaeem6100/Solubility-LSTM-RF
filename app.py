import os

from flask import Flask, request, render_template, send_from_directory

from helper import Predictor

app = Flask(__name__)


@app.route('/<path:page>')
def show(page):
    return render_template('%s.html' % page)


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
@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'), 'favicon.ico',
                               mimetype='image/vnd.microsoft.icon')


@app.errorhandler(404)
def not_found(error):
    return "Not Found", 404


if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(debug=False, host="0.0.0.0", port=port)
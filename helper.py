import numpy as np
from keras.models import load_model
import pickle


class Predictor:
    def __init__(self):
        pass

    @staticmethod
    def prot_matrix(seq):
        encoder = ['X', 'A', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'K', 'L', 'M', 'N', 'P', 'Q', 'R', 'S', 'T', 'V', 'W',
                   'Y']
        svv = [0 for x in range(len(seq))]
        i = 0
        for i in range(len(seq)):
            value = encoder.index(seq[i])
            svv[i] = value
        return svv

    def readingSequence(self, seq):
        seq = seq.replace('B', 'D')
        seq = seq.replace('U', 'C')
        seq = seq.replace('Z', 'Q')
        seq = seq.replace('O', 'K')
        total_xes = 3000 - len(seq)
        total_xes = "X" * total_xes
        seq = seq.upper() + total_xes
        tem = seq.rstrip()
        return self.prot_matrix(tem)

    @staticmethod
    def LSTMInit():
        model = load_model('lstmFeatureModel.h5')
        # return tf.keras.models.load_model("lstmFeatures.h5")
        return model

    @staticmethod
    def RFInit():
        with open("randomforestModel.pkl", 'rb') as file:
            clf = pickle.load(file)
            return clf

    def LSTMPredict(self, seq):
        model = self.LSTMInit()
        seq = self.readingSequence(seq)
        seq = np.array(seq)
        seq = seq.reshape(1, 3000)
        pred = model.predict(seq)
        return pred


if __name__ == '__main__':
    pred = Predictor()
    seq = "MGSVRKASAWLGLVDDNDDERYYDDDYAEGQESGEAWVTDPRVKVASETAEEKGRRIGTVTPDSFRDARGIGELFRDGVPVIINLTAMEPTDAKRVVDFAAGLTFGLRGTIERVATRVFLLTPANTEIVSGEAAGRPTDGFFNQS"
    clf = pred.RFInit()
    data = clf.predict(pred.LSTMPredict(seq))
    print(data[0])

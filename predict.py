from tensorflow.keras.models import Model, load_model
from kapre.time_frequency import Melspectrogram, Spectrogram
from scipy.io import wavfile
import os
import librosa
import numpy as np
import SpeechModels
import audioUtils
import pickle
import heapq
from python_speech_features import mfcc
import pandas as pd
import time
import regex
from regex import color
import Record
GSCmdV2Categs = {
    'Bat': 0,
    'Tat': 1,
    'Sang Hon': 2,
    'Mo Di': 3,
    'Toi Hon': 4,
    'Chuyen': 5,
    'Len': 6,
    'Xuong': 7,
    'Keo Len': 8,
    'Keo Xuong': 9,
    'Dong': 10,
    'Mo': 11,
    'Den': 12,
    'Tivi': 13,
    'Quat': 14,
    'Phong Bep': 15,
    'Rem Cua': 16,
    'Thang May': 17,
    'Cua': 18,
    '1': 19,
    '2': 20,
    '3': 21,
    '4': 22,
    '5': 23,
    '6': 24,
    '7': 25,
    '8': 26,
    '9': 27,
    '10': 28,
    '11': 29,
    '12': 30,
    '13': 31,
    '14': 32,
    '15': 33,
    '16': 34,
    '17': 35,
    '18': 36,
    '19': 37,
    '20': 38,
    '21': 39,
    '22': 40,
    '23': 41,
    '24': 42,
    '25': 43,
    '26': 44,
    '27': 45,
    '28': 46,
    '29': 47,
    '30': 48,
    'Tang': 49,
    'Giam': 50,
    'Do Sang': 51,
    'Phong Khach': 52,
    'Phong Ngu': 53,
    'Phong Tam': 54
}

# GSCmdV2Categs = {
#     'Bat': 0,
#     'Tat': 1,
#     'SangHon': 2,
#     'MoDi': 3,
#     'ToiHon': 4,
#     'Chuyen': 5,
#     'Len': 6,
#     'Xuong': 7,
#     'KeoLen': 8,
#     'KeoXuong': 9,
#     'Dong': 10,
#     'Mo': 11,
#     'Den': 12,
#     'Tivi': 13,
#     'Quat': 14,
#     'Bep': 15,
#     'RemCua': 16,
#     'ThangMay': 17,
#     'Cua': 18,
#     '1': 19,
#     '2': 20,
#     '3': 21,
#     '4': 22,
#     '5': 23,
#     '6': 24,
#     '7': 25,
#     '8': 26,
#     '9': 27,
#     '10': 28,
#     '11': 29,
#     '12': 30,
#     '13': 31,
#     '14': 32,
#     '15': 33,
#     '16': 34,
#     '17': 35,
#     '18': 36,
#     '19': 37,
#     '20': 38,
#     '21': 39,
#     '22': 40,
#     '23': 41,
#     '24': 42,
#     '25': 43,
#     '26': 44,
#     '27': 45,
#     '28': 46,
#     '29': 47,
#     '30': 48,
#     'Tang': 49,
#     'Giam': 50,
#     'DoSang': 51,
#     'Khach': 52,
#     'Ngu': 53,
#     'Tam': 54
# }

nCategs = 55
sr = 16000

model = SpeechModels.AttRNNSpeechModel(
    nCategs, samplingrate=sr, inputLength=16000)
model.compile(optimizer='adam', loss=[
              'sparse_categorical_crossentropy'], metrics=['sparse_categorical_accuracy'])
model.load_weights('model_TV_20200625.h5')
print("Load model successfully!")


def get_test_file(test_file, gmms):
    """
        Test a given file and predict an label for it.
    """
    rate, sig = wavfile.read(test_file)
    mfcc_feat = mfcc(sig, rate)
    pred = {}
    for model in gmms:
        pred[model] = gmms[model].score(mfcc_feat)
    return get_nbest(pred, 2), pred


def get_nbest(d, n):
    """
        Utility function to return n best predictions.
    """
    return heapq.nlargest(n, d, key=lambda k: d[k])


def predict_label(test_file, model_path="gmmhmm.pkl"):
    """
        Description:
            predict label for input wav file.

        Params:
            * test_file (mandatory): Wav file for which label should be predicted.
            * model_path: Path to gmmhmm model.

        Return:
            A list of predicted label and next best predicted label.
    """
    gmms = pickle.load(open(model_path, "rb"), encoding='latin1')
    predicted = get_test_file(test_file, gmms)
    return predicted


def predict(file_path):
    try:
        start = time.time()
        data = audioUtils.process_data(file_path)
        #print("Process time", time.time() - start)
        if len(data) > 16000:
            data = data[0:16000]
        
        print("LEN",len(data))
        X = np.empty((1, len(data)))
        X[0] = data

        out = model.predict(X)

        inv_map = {v: k for k, v in GSCmdV2Categs.items()}
        pred_label = inv_map[np.argmax(out[0])]
        #print(file_path, pred_label)
        accuracy = max(out[0])
        #print("accuracy", accuracy)

        #client.publish("predict", inv_map[np.argmax(out[0])])
        # Record.record_to_file(data, 2, pred_label, accuracy, 16000)
        return pred_label, accuracy

    except:
        print("An exception occurred")
        raise
def t_predict(data):
    try:
        start = time.time()
        data = audioUtils.t_process_data(data)
        print("Process time", time.time() - start)
        l = len(data)
        if l > 16000:
            data = data[0:16000]
        if l < 16000:
            print("<16000:", l)
            for i in range (l,16000):
                data.append(0)
        X = np.empty((1, len(data)))
        X[0] = data

        out = model.predict(X)

        inv_map = {v: k for k, v in GSCmdV2Categs.items()}
        pred_label = inv_map[np.argmax(out[0])]
        accuracy = max(out[0])
        # Record.record_to_file(data, 2, pred_label, accuracy, 16000)
        print("predict", pred_label)
        print("accuracy", accuracy)
        #client.publish("predict", pred_label)
        if accuracy > 0.5:
            cmd = regex.get_cmd(pred_label)
            if cmd != "":
                print(color.BOLD +"                                                                                  " + cmd + color.END)
        return pred_label, accuracy

    except:
        print("An exception occurred")
        raise

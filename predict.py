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
import paho.mqtt.client as mqtt
import pandas as pd
import time
import regex

def on_connect(client, userdata, flags, rc):
    print("Connected with result code " + str(rc))

    # Subscribing in on_connect() means that if we lose the connection and
    # reconnect then subscriptions will be renewed.
    client.subscribe("#")


def on_message(client, userdata, msg):
    print(msg.topic + " " + str(msg.payload))


client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect_async("10.0.55.170", 1883, 60)
client.loop_start()

GSCmdV2Categs = {
    'Bat': 0,
    'Tat': 1,
    'SangHon': 2,
    'MoDi': 3,
    'ToiHon': 4,
    'Chuyen': 5,
    'Len': 6,
    'Xuong': 7,
    'KeoLen': 8,
    'KeoXuong': 9,
    'Dong': 10,
    'Mo': 11,
    'Den': 12,
    'Tivi': 13,
    'Quat': 14,
    'Bep': 15,
    'RemCua': 16,
    'ThangMay': 17,
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
    '30': 48
}

nCategs = 49
sr = 16000

model = SpeechModels.AttRNNSpeechModel(
    nCategs, samplingrate=sr, inputLength=16000)
model.compile(optimizer='adam', loss=[
              'sparse_categorical_crossentropy'], metrics=['sparse_categorical_accuracy'])
model.load_weights('model_TV.h5')
print("Load model successfully!")
cmd = ""

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
        audioUtils.process_data(file_path)
        print("Process time", time.time() - start)

        y, sr = librosa.load(file_path, sr=None)
        np_file = file_path + '.npy'
        np.save(np_file, y)

        sample_rate, samples = wavfile.read(file_path)
        X = np.empty((1, len(samples)))

        input_file = np.load(np_file)
        os.remove(np_file)
        X[0] = input_file

        out = model.predict(X)

        inv_map = {v: k for k, v in GSCmdV2Categs.items()}
        print(file_path + " : " + inv_map[np.argmax(out[0])])
        print("accuracy", max(out[0]))

        client.publish("predict", inv_map[np.argmax(out[0])])

        return inv_map[np.argmax(out[0])]

    except:
        print("An exception occurred")
        raise


# conf_file = "input.txt"
# inputs = pd.read_csv(conf_file, sep=" ", header=None)[0].tolist()
# for f in inputs:
#     predict(f)


def t_predict(data):
    try:
        start = time.time()
        data = audioUtils.t_process_data(data)
        print("Process time", time.time() - start)
        X = np.empty((1, 16000))
        X[0] = data

        out = model.predict(X)

        inv_map = {v: k for k, v in GSCmdV2Categs.items()}
        pred_label = inv_map[np.argmax(out[0])]
        print("predict", pred_label)
        print("accuracy", max(out[0]))

        client.publish("predict", pred_label)

        global cmd

        cmd += pred_label
        code, res, cmd = regex.get_cmd(cmd)
        if code > 0:
            print("Command", cmd)
            
        return pred_label

    except:
        print("An exception occurred")
        raise

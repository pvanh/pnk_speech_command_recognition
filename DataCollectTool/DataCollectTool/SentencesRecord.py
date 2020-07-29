import os
import struct
import wave
from array import array
from sys import byteorder

import matplotlib.pyplot as plt
import numpy as np

import connector as cnt
import CommandRecord as cm
import pyaudio

cursor = cnt.my_db.cursor()
cursor.execute("select * from record_sentences.sentences")

SENTENCES_LIST = cursor.fetchall()

for data_ in SENTENCES_LIST:
    print(data_[1])

PATH = ""
CUR_SENTENCES = 0

end = False
is_recording = False
paused = False
save = False


def record_to_file(data, sample_width, recorder_name):
    # sample_width, data = record()

    _data = struct.pack('<' + ('h' * len(data)), *data)
    file_num = len([
        name for name in os.listdir(PATH + '/' + SENTENCES_LIST[CUR_SENTENCES][0])
        if (name.endswith('.wav') and recorder_name in name)
    ])

    wf = wave.open(
        PATH + '/' + SENTENCES_LIST[CUR_SENTENCES][0] + '/' + recorder_name + '_' + str(file_num) + '.wav',
        'wb')
    wf.setnchannels(1)
    wf.setsampwidth(sample_width)
    wf.setframerate(cm.RATE)

    # for i in data:
    #     i = struct.pack('<h', i)
    #     wf.writeframes(i)

    wf.writeframes(_data)

    wf.close()


def record():
    """Record a word or words from the microphone and
    return the data as an array of signed shorts.

    Normalizes the audio, trims silence from the
    start and end, and pads with 0.5 seconds of
    blank sound to make sure it won't get chopped off."""

    global is_recording, end, paused, save, CUR_SENTENCES
    p = pyaudio.PyAudio()
    stream = p.open(
        format=cm.FORMAT,
        channels=cm.CHANNELS,
        rate=cm.RATE,
        input=True,
        output=True,
        frames_per_buffer=cm.CHUNK
    )

    num_silent = 0

    r = array('h')
    prev = array('h')

    plt.ion()
    fig, ax = plt.subplots()

    x = np.arange(0, cm.CHUNK)
    line, = ax.plot(x, np.random.rand(cm.CHUNK))
    ax.set_ylim([-2 ** 9, (2 ** 9 - 1)])

    while True:

        if end:
            stream.stop_stream()
            stream.close()
            p.terminate()
            plt.close(fig)
            break

        if save:
            sample_width = p.get_sample_size(cm.FORMAT)
            r = cm.normalize(r)
            r = cm.trim(r)
            r = cm.add_silence(r, 0.2)
            record_to_file(r, sample_width, cm.NAME)
            r = array('h')
            CUR_SENTENCES = CUR_SENTENCES + 1
            if CUR_SENTENCES == len(SENTENCES_LIST):
                end = True
            continue

        if not paused:
            record_data = array('h', stream.read(cm.CHUNK))
            if byteorder == 'big':
                record_data.byteswap()
            # data = struct.unpack(str(CHUNK) + 'h', stream.read(CHUNK))
            line.set_ydata(record_data)
            fig.canvas.draw()
            fig.canvas.flush_events()

            # r.extend(record_data)

            silent = cm.is_silent(record_data)

            if silent and is_recording:
                num_silent += 1
                r.extend(record_data)
                if num_silent > 20:
                    is_recording = False
                    num_silent = 0

            elif not silent:
                if not is_recording:
                    is_recording = True
                    r.extend(prev)
                    # print('Đang ghi âm')
                r.extend(record_data)

            prev = record_data

#
# if __name__ == '__main__':
#     print("Start")
#     record()

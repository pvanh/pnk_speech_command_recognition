import os
import os.path
import struct
import sys
import time
import wave
from array import array
from sys import byteorder

import matplotlib.pyplot as plt
import numpy as np
import pyaudio
import DataCollectTool.CountingDialog as CountingDialog
from PyQt5.QtWidgets import QDialog


# Dialog
class CountingForm(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = CountingDialog.Ui_CountingDialog()
        self.ui.setupUi(self)
        self.show()

    def update_cmdLabel(self, cmdStr):
        self.ui.command_lbl.setText(cmdStr)

    def update_timesLabel(self, timesStr):
        self.ui.times_remain_lbl.setText(timesStr)

    def update_nameLabel(self, nameStr):
        self.ui.name_lbl.setText(nameStr)

    def update_statusLabel(self, sttStr):
        self.ui.status_lbl.setText(sttStr)


# number of audio frame will be processed and displayed at a time

p = pyaudio.PyAudio()

CHUNK = 1024 * 3

THRESHOLD = 300
FORMAT = pyaudio.paInt16
CHANNELS = 1
# sample per second
RATE = int(p.get_device_info_by_index(1)["defaultSampleRate"])

COMMAND = ["Bật", "Tắt", "Sáng hơn", "Mờ đi",
           "Tối hơn", "Chuyển", "Lên", "Xuống", "Kéo lên",
           "Kéo xuống", "Đóng", "Mở", "Đèn", "Ti vi", "Quạt", "Bếp", "Rèm cửa",
           "Thang máy", "Cửa", "1", "2", "3", "4", "5",
           "6", "7", "8", "9", "10", "11", "12",
           "13", "14", "15", "16", "17", "18", "19",
           "20", "21", "22", "23", "24", "25",
           "26", "27", "28", "29", "30", "Tăng", "Giảm",
           "Độ sáng", "Khách", "Ngủ", "Tắm", "Tầng"]

DIRECTORY = ["Bat", "Tat", "SangHon", "MoDi", "ToiHon",
             "Chuyen", "Len", "Xuong", "KeoLen", "KeoXuong",
             "Dong", "Mo", "Den", "Tivi", "Quat", "Bep",
             "RemCua", "ThangMay", "Cua", "So1", "So2", "So3",
             "So4", "So5", "So6", "So7", "So8", "So9", "So10",
             "So11", "So12", "So13", "So14", "So15", "So16",
             "So17", "So18", "So19", "So20", "So21", "So22",
             "So23", "So24", "So25", "So26", "So27", "So28",
             "So29", "So30", "Tang", "Giam", "DoSang", "Khach", "Ngu",
             "Tam", "Tang_Vitri"]

# INSERT YOUR PATH HERE
PATH = ""
NAME = ""
CUR_COMMAND = 0
CUR_DIRECTORY = 0
TIMES_RECORDED = 0
TIMES_NEEDED = 0
count = 1

is_recording = False
end = True


def is_silent(record_data):
    return max(record_data) < THRESHOLD


def normalize(record_data):
    """Average the volume out"""
    MAX = 16384
    times = float(MAX) / max(abs(i) for i in record_data)

    r = array('h')
    for i in record_data:
        r.append(int(i * times))
    return r


def trim(record_data):
    def _trim(rc_data):
        record_start = False
        r = array('h')

        for i in rc_data:
            if not record_start and abs(i) > THRESHOLD:
                record_start = True
                r.append(i)
            elif record_start:
                r.append(i)
        return r

    record_data = _trim(record_data)

    record_data.reverse()
    record_data = _trim(record_data)
    record_data.reverse()
    return record_data


def add_silence(record_data, seconds):
    """Add some seconds of silence to the start and end of
    the processed command so that it won't get chopped off"""
    silence = [0] * int(seconds * RATE)
    r = array('h', silence)
    r.extend(record_data)
    r.extend(silence)
    return r


def record():
    """Record a word or words from the microphone and
    return the data as an array of signed shorts.

    Normalizes the audio, trims silence from the
    start and end, and pads with 0.5 seconds of
    blank sound to make sure it won't get chopped off."""

    # dialog = QApplication(sys.argv)
    d = CountingForm()
    d.show()

    global is_recording, CUR_COMMAND, TIMES_RECORDED, CUR_DIRECTORY, end, count
    # p = pyaudio.PyAudio()
    stream = p.open(
        format=FORMAT,
        channels=CHANNELS,
        rate=RATE,
        input=True,
        output=True,
        frames_per_buffer=CHUNK,
        output_device_index=0
    )

    num_silent = 0

    r = array('h')
    prev = array('h')

    plt.ion()
    fig, ax = plt.subplots()

    x = np.arange(0, CHUNK)
    line, = ax.plot(x, np.random.rand(CHUNK))
    ax.set_ylim([-2 ** 9, (2 ** 9 - 1)])

    d.update_nameLabel(NAME)
    d.update_cmdLabel(COMMAND[CUR_COMMAND])
    d.update_timesLabel(str(TIMES_RECORDED))
    d.update_statusLabel("Sẵn sàng")
    # print("Tên:" + NAME)
    # print("Lệnh: " + COMMAND[CUR_COMMAND])
    # print("Số lần thu âm: " + str(TIMES_RECORDED))
    while True:
        if end:
            stream.stop_stream()
            stream.close()
            # p.terminate()
            plt.close(fig)
            break
        record_data = array('h', stream.read(CHUNK, exception_on_overflow=False))
        if byteorder == 'big':
            record_data.byteswap()
        # data = struct.unpack(str(CHUNK) + 'h', stream.read(CHUNK))
        line.set_ydata(record_data)
        fig.canvas.draw()
        fig.canvas.flush_events()

        # r.extend(record_data)

        silent = is_silent(record_data)

        if TIMES_RECORDED == TIMES_NEEDED:
            TIMES_RECORDED = 0
            stream.stop_stream()
            stream.close()
            # p.terminate()
            plt.close(fig)
            break

        if silent and is_recording:
            num_silent += 1
            r.extend(record_data)
            if num_silent > 10:
                is_recording = False
                num_silent = 0
                # print('Xong')
                # d.update_statusLabel("Đang lưu")

                sample_width = p.get_sample_size(FORMAT)

                # normalize_start = time.clock()
                r = normalize(r)
                # normalize_end = time.clock()
                # print("Normalize: ", normalize_end - normalize_start);
                #
                # trim_start = time.clock()
                r = trim(r)
                # trim_end = time.clock()
                # print("Trim: ", trim_end - trim_start)
                #
                r = add_silence(r, 0.2)
                #
                # write_start = time.clock()
                record_to_file(r, sample_width, NAME)
                # write_end = time.clock()
                # print("Write: ", write_end - write_start)
                # TIMES_RECORDED = TIMES_RECORDED + 1
                CUR_DIRECTORY = CUR_DIRECTORY + 1
                CUR_COMMAND = CUR_COMMAND + 1
                if CUR_COMMAND > 55 and CUR_DIRECTORY > 55:
                    CUR_COMMAND = 0
                    CUR_DIRECTORY = 0
                    TIMES_RECORDED = TIMES_RECORDED + 1

                    # end = True
                    # stream.stop_stream()
                    # stream.close()
                    # p.terminate()
                    # plt.close(fig)
                    # break

                # if TIMES_RECORDED >= 10:
                #     TIMES_RECORDED = 0
                #     CUR_DIRECTORY = CUR_DIRECTORY + 1
                #     CUR_COMMAND = CUR_COMMAND + 1
                #
                #     # count = count + 1
                #     # if CUR_COMMAND > 54 and CUR_DIRECTORY > 54:
                #     #     CUR_COMMAND = 0
                #     #     CUR_DIRECTORY = 0
                #     # if count >= 10:
                #     #     count = 1
                #     #     end = True
                #     #     stream.stop_stream()
                #     #     stream.close()
                #     #     p.terminate()
                #     #     plt.close(fig)
                #     #     break
                #     if CUR_COMMAND > 55 and CUR_DIRECTORY > 55:
                #         CUR_COMMAND = 0
                #         CUR_DIRECTORY = 0
                #         end = True
                #         stream.stop_stream()
                #         stream.close()
                #         p.terminate()
                #         plt.close(fig)
                #         break
                r = array('h')
                d.update_cmdLabel(COMMAND[CUR_COMMAND])
                d.update_timesLabel(str(TIMES_RECORDED))
                d.update_statusLabel("Sẵn sàng")
                # print("Tên:" + NAME)
                # print("Lệnh: " + COMMAND[CUR_COMMAND])
                # print("Số lần thu: " + str(TIMES_RECORDED))
        elif not silent:
            if not is_recording:
                is_recording = True
                r.extend(prev)
                # print('Đang ghi âm')
                d.update_statusLabel("Đang ghi âm")
            r.extend(record_data)

        prev = record_data

    # sys.exit(dialog.exec_())

    # stream.stop_stream()
    # stream.close()
    # p.terminate()

    # print("before trim: " + str(r))

    # print("before normalize: " + str(r))
    # print("before add silence: " + str(r))

    # return sample_width, r


def record_to_file(data, sample_width, recorder_name):
    # sample_width, data = record()

    _data = struct.pack('<' + ('h' * len(data)), *data)
    file_num = len([
        name for name in os.listdir(PATH + '/' + DIRECTORY[CUR_DIRECTORY])
        if (name.endswith('.wav') and recorder_name in name)
    ])

    wf = wave.open(PATH + '/' + DIRECTORY[CUR_DIRECTORY] + '/' + recorder_name + '_' + str(file_num) + '.wav', 'wb')
    wf.setnchannels(1)
    wf.setsampwidth(sample_width)
    wf.setframerate(RATE)

    # write_start = time.clock()
    # for i in data:
    #     i = struct.pack('<h', i)
    #     wf.writeframes(i)
    wf.writeframes(_data)
    # write_end = time.clock()
    # print("Write Loop: ", write_end - write_start)
    wf.close()


# if __name__ == '__main__':
#     print("Say something")
#     record()
#     print("Done")

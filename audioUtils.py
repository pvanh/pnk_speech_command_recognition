"""
Utility functions for audio files
"""
import librosa
import os
from tqdm import tqdm
import numpy as np
import matplotlib.pyplot as plt
import itertools
from pydub import AudioSegment
from scipy.io import wavfile


def plot_confusion_matrix(cm, classes,
                          normalize=False,
                          title='Confusion matrix',
                          cmap=plt.cm.Blues):
    """
    This function prints and plots the confusion matrix.
    Normalization can be applied by setting `normalize=True`.
    """
    if normalize:
        cm = cm.astype('float') / cm.sum(axis=1)[:, np.newaxis]
        print("Normalized confusion matrix")
    else:
        print('Confusion matrix, without normalization')

    plt.figure(figsize=(15, 15))
    plt.imshow(cm, interpolation='nearest', cmap=cmap)
    plt.title(title, fontsize=30)
    plt.colorbar()
    tick_marks = np.arange(len(classes))
    plt.xticks(tick_marks, classes, rotation=45, fontsize=15)
    plt.yticks(tick_marks, classes, fontsize=15)

    fmt = '.3f' if normalize else 'd'
    thresh = cm.max() / 2.
    for i, j in itertools.product(range(cm.shape[0]), range(cm.shape[1])):
        plt.text(j, i, format(cm[i, j], fmt), size=11,
                 horizontalalignment="center",
                 color="white" if cm[i, j] > thresh else "black")

    plt.ylabel('True label', fontsize=30)
    plt.xlabel('Predicted label', fontsize=30)
    plt.savefig('picConfMatrix.png', dpi=400)
    plt.tight_layout()


def WAV2Numpy(folder, sr=None):
    """
    Recursively converts WAV to numpy arrays.
    Deletes the WAV files in the process

    folder - folder to convert.
    """
    allFiles = []
    for root, dirs, files in os.walk(folder):
        allFiles += [os.path.join(root, f) for f in files
                     if f.endswith('.wav')]

    for file in tqdm(allFiles):
        y, sr = librosa.load(file, sr=None)

        # if we want to write the file later
        # librosa.output.write_wav('file.wav', y, sr, norm=False)
        np.save(file + '.npy', y)
        os.remove(file)


def detect_leading_silence(sound, silence_threshold=-40.0, chunk_size=10):
    '''
    sound is a pydub.AudioSegment
    silence_threshold in dB
    chunk_size in ms

    iterate over chunks until you find the first one with sound
    '''
    trim_ms = 0  # ms

    assert chunk_size > 0  # to avoid infinite loop
    while sound[trim_ms:trim_ms+chunk_size].dBFS < silence_threshold and trim_ms < len(sound):
        trim_ms += chunk_size

    return trim_ms


def process_data(file_path):
    sound = AudioSegment.from_file(file_path, format="wav")
    sound = sound.set_frame_rate(16000)
    sound = sound.set_channels(1)
    sound = sound.set_sample_width(2)

    duration = len(sound)

    out_sound = sound
    
    if duration < 1000:
        offset = 1000 - duration
        silence_sound = AudioSegment.silent(duration=offset)
        out_sound = silence_sound + sound

    else:
        start_trim = detect_leading_silence(sound)
        #end_trim = detect_leading_silence(sound.reverse(), silence_threshold = -42.0)
        end_trim = detect_leading_silence(sound.reverse())

        l = duration - end_trim - start_trim


        if l < 10:
            print("Sound in audio is too short")

        if l > 1000:
            print("Warning: Sound in audio is too long")
            out_sound = sound[start_trim:start_trim + 1000]

            #out_sound = sound[start_trim:duration - end_trim]

        else:
            offset = 1000 - l
            start = 0
            end = duration

            if start_trim >= offset:
                start = start_trim - offset
                end = start + 1000
            else:
                start = 0
                end = 1000

            out_sound = sound[start:end]


    out_sound.export(file_path, format="wav")

    # sample_rate, samples = wavfile.read(file_path)
    # if len(samples) > 16000:
    #     out_sound = out_sound[0:len(out_sound) - 1]
    
    # out_sound.export(file_path, format="wav")

    #print("Process audio successfully!")


def t_process_data(data):
    sound = AudioSegment(data.tobytes(), 
                    frame_rate=44100,
                    sample_width=2, 
                    channels=1)
                    
    sound = sound.set_frame_rate(16000)
    sound = sound.set_channels(1)
    sound = sound.set_sample_width(2)

    duration = len(sound)

    out_sound = sound
    
    if duration < 1000:
        offset = 1000 - duration
        silence_sound = AudioSegment.silent(duration=offset)
        out_sound = silence_sound + sound

    else:
        start_trim = detect_leading_silence(sound)
        #end_trim = detect_leading_silence(sound.reverse(), silence_threshold = -42.0)
        end_trim = detect_leading_silence(sound.reverse())

        l = duration - end_trim - start_trim


        if l < 10:
            print("Sound in audio is too short")

        if l > 1000:
            print("Warning: Sound in audio is too long")
            out_sound = sound[start_trim:start_trim + 1000]

            #out_sound = sound[start_trim:duration - end_trim]

        else:
            offset = 1000 - l
            start = 0
            end = duration

            if start_trim >= offset:
                start = start_trim - offset
                end = start + 1000
            else:
                start = 0
                end = 1000

            out_sound = sound[start:end]

    samples = out_sound.get_array_of_samples()

    return samples
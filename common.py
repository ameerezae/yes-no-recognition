import os
from re import search
import soundfile
import numpy as np


def get_files(path):
    if os.path.exists(path):
        return os.listdir(path)
    else:
        raise FileNotFoundError

def is_contain(sub_string, full_string):
    if search(sub_string, full_string):
        return True
    else:
        return False

def power_spectrum_magnitude(signal):
    return np.sum(signal ** 2)

def yes_no_recognition(file_path, threshold, multiple_chanel=False):
    low_freq = [0, None]
    high_freq = [None, None]
    data, rate = soundfile.read(file_path)
    min_energy = 10
    if multiple_chanel is True:
        data = data[:, 0]
    energy = power_spectrum_magnitude(data)
    if energy < min_energy:
        return "Mute", 0

    fourier_transform_data = np.fft.fft(data, rate)
    magnitude_data = np.round(np.abs(fourier_transform_data))
    low_freq[1] = ((len(data) * 5512) // rate)
    high_freq[0] = low_freq[1]
    high_freq[1] = ((len(data) * 11025) // rate)
    sum_low_freq = np.sum(magnitude_data[low_freq[0]: low_freq[1]])
    sum_high_freq = np.sum(magnitude_data[high_freq[0]: high_freq[1]])
    if sum_high_freq != 0:
        feature_value = sum_low_freq // sum_high_freq
    else:
        feature_value = sum_low_freq
    if threshold is None:
        return feature_value

    if feature_value < threshold:
        return "yes", feature_value
    else:
        return "no", feature_value
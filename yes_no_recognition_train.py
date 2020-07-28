import os
import soundfile
import numpy as np
from common import is_contain, get_files, yes_no_recognition, power_spectrum_magnitude


if __name__ == '__main__':
    train_file_name = "train"
    correct = {"no": 0, "yes": 0}
    incorrect = {"no": 0, "yes": 0}
    threshold = 20
    average_energy = 0
    signals_energy = []
    sounds_file = get_files(train_file_name)
    for sound_file in sounds_file:
        file_path = os.path.join(train_file_name, sound_file)
        data, rate = soundfile.read(file_path)
        data = data[:, 0]
        signals_energy.append(power_spectrum_magnitude(data))
        result, f_value = yes_no_recognition(file_path, threshold=threshold, multiple_chanel=True)
        if result == "yes":
            if is_contain("no", sound_file):
                incorrect["no"] += 1
            elif is_contain("yes", sound_file):
                correct["yes"] += 1
        elif result == "no":
            if is_contain("no", sound_file):
                correct["no"] += 1
            elif is_contain("yes", sound_file):
                incorrect["yes"] += 1
        else:
            if is_contain("no", sound_file):
                incorrect["no"] += 1
            elif is_contain("yes", sound_file):
                incorrect["yes"] += 1

    OKGREEN = '\033[92m'
    UNDERLINE = '\033[4m'
    ENDC = '\033[0m'
    FAIL = '\033[91m'
    BOLD = '\033[1m'
    OKBLUE = '\033[94m'
    average_energy = np.average(signals_energy)
    success_percent_of_yes = (correct["yes"] / (correct["yes"] + incorrect["yes"])) * 100
    success_percent_of_no = (correct["no"] / (correct["no"] + incorrect["no"])) * 100
    total_success_percent = ((correct["yes"]+correct["no"]) / (len(sounds_file))) * 100
    print("{}Correct Answers of {}yes{} {}is: {}{}".format(OKGREEN, UNDERLINE, ENDC, OKGREEN, BOLD, correct["yes"]))
    print("{}Incorrect Answers of {}yes{} {}is: {}{}".format(FAIL, UNDERLINE, ENDC, FAIL, BOLD, incorrect["yes"]))
    print("{}Correct Answers of {}no{} {}is: {}{}".format(OKGREEN, UNDERLINE, ENDC, OKGREEN, BOLD, correct["no"]))
    print("{}Incorrect Answers of {}no{} {}is: {}{}".format(FAIL, UNDERLINE, ENDC, FAIL, BOLD, incorrect["no"]))
    print("{}Total correct Answers is: {}{}".format(OKGREEN, BOLD, correct["no"] + correct["yes"]))
    print("{}Total incorrect Answers is: {}{}".format(FAIL, BOLD, incorrect["yes"] + incorrect["no"]))
    print("{}Success percent of {}yes{} {}is: {}{}".format(OKBLUE, UNDERLINE, ENDC, OKBLUE, BOLD, success_percent_of_yes))
    print("{}Success percent of {}no{} {}is: {}{}".format(OKBLUE, UNDERLINE, ENDC, OKBLUE, BOLD, success_percent_of_no))
    print("{}Total success percent is: {}{}".format(OKBLUE, BOLD, total_success_percent))
    print("{}Average energy is: {}{}".format(OKGREEN, average_energy, ENDC))

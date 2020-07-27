import os
import matplotlib.pyplot as plot
from common import yes_no_recognition, get_files, is_contain


if __name__ == '__main__':
    train_file_name = "train"
    sounds_file = get_files(train_file_name)
    features_value = {"yes": [], "no": []}
    count_of_feature_value = {"yes": {}, "no": {}}
    for sound_file in sounds_file:
        file_path = os.path.join(train_file_name, sound_file)
        feature_value = yes_no_recognition(file_path, threshold=None, multiple_chanel=True)
        if is_contain("no", sound_file):
            if feature_value not in count_of_feature_value["no"].keys():
                count_of_feature_value["no"][feature_value] = 1
            else:
                count_of_feature_value["no"][feature_value] += 1
            features_value["no"].append(feature_value)
        elif is_contain("yes", sound_file):
            if feature_value not in count_of_feature_value["yes"].keys():
                count_of_feature_value["yes"][feature_value] = 1
            else:
                count_of_feature_value["yes"][feature_value] += 1
            features_value["yes"].append(feature_value)

    plot.figure(figsize=(10, 10))
    plot.subplot(2, 1, 1)
    plot.bar(list(count_of_feature_value["yes"].keys()), list(count_of_feature_value["yes"].values()))
    plot.title("yes")
    plot.xlabel("feature value")
    plot.ylabel("count of feature value")

    plot.subplot(2, 1, 2)
    plot.bar(list(count_of_feature_value["no"].keys()), list(count_of_feature_value["no"].values()))
    plot.title("no")
    plot.xlabel("feature value")
    plot.ylabel("count of feature value")
    plot.savefig("result_features_value.png")

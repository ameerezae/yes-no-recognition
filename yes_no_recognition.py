import pyaudio
import wave
from common import yes_no_recognition


chunk = 1024  # record in chunks of 1024 samples
sample_format = pyaudio.paInt16  # 16 bits per sample
channels = 1  # number of channels
rate = 44100  # record at 44100 samples per second
seconds = 2  # recording time
threshold = 20
filename = "voice.wav"
OKGREEN = '\033[92m'
WARNING = '\033[93m'
ENDC = '\033[0m'
p_audio = pyaudio.PyAudio()


while True:
    # recording data
    stream = p_audio.open(format=sample_format,
                          channels=channels,
                          rate=rate,
                          frames_per_buffer=chunk,
                          input=True)

    frames = []  # Initialize array to store frames

    # store data in chunks for 0.5 seconds
    for i in range(0, int(rate / chunk * seconds)):
        data = stream.read(chunk)
        frames.append(data)

    # stop and close the stream
    stream.stop_stream()
    stream.close()

    # write data to a file
    wf = wave.open(filename, 'wb')
    wf.setnchannels(channels)
    wf.setsampwidth(p_audio.get_sample_size(sample_format))
    wf.setframerate(rate)
    wf.writeframes(b''.join(frames))
    wf.close()

    # reading file
    result, feature_value = yes_no_recognition(filename, threshold)
    if result != "Mute":
        print("{}Recognized:{}".format(WARNING, ENDC), "{}{}{}".format(OKGREEN, result, ENDC), "", end='\r')
    else:
        print("{}Listening:{}".format(WARNING, ENDC), "{}{}{}".format(OKGREEN, result, ENDC), "", end='\r')

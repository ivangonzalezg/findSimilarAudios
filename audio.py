import sys
import numpy as np
import librosa as lr
from glob import glob

# Audio to compare

userAudioDir = "./userAudio.wav"
userAudio, userFrequency = lr.load(userAudioDir)

# Comparator

audiosDir = "./originalAudios"
audioFiles = glob(audiosDir + "/*.wav")
maxCorrelation = 0
maxName = ""
maxType = ""
counter = 1
for x in range(len(audioFiles)):
    testAudio, testFrequency = lr.load(audioFiles[x])
    lenDifference = len(userAudio) - len(testAudio)
    if lenDifference > 0:
        correlation = np.corrcoef(userAudio[0:len(testAudio)], testAudio)
        if correlation[1][0] > maxCorrelation:
            maxCorrelation = correlation[1][0]
            maxName = audioFiles[x].split("/")[2].split(".")[0]
    elif lenDifference < 0:
        correlation = np.corrcoef(testAudio[0:len(userAudio)], userAudio)
        if correlation[1][0] > maxCorrelation:
            maxCorrelation = correlation[1][0]
            maxName = audioFiles[x].split("/")[2].split(".")[0]
    else:
        correlation = np.corrcoef(userAudio, testAudio)
        if correlation[1][0] > maxCorrelation:
            maxCorrelation = correlation[1][0]
            maxName = audioFiles[x].split("/")[2].split(".")[0]
    sys.stdout.write("\r" + "Buscando" + "." * counter)
    counter += 1
    if counter > 3:
        counter = 1

sys.stdout.write("\n")
if maxName.split("_")[0] == "ECG":
    maxType = "Señal Electrocardiográfica"
elif maxName.split("_")[0] == "EMG":
    maxType = "Señal Electromiográfica"
elif maxName.split("_")[0] == "EEG":
    maxType = "Señal Electroencefalográfica"

print("Tipo: " + maxType)

from glob import glob
import numpy as np
import librosa as lr

#Audio a comparar

userAudioDir = "./userAudio.wav"
userAudio, userFrequency = lr.load(userAudioDir)

#Comparador

audiosDir = "./originalAudios"
audioFiles = glob(audiosDir + "/*.wav")
maxCorrelation = 0
maxName = ""
for x in range(len(audioFiles)):
    testAudio, testFrequency = lr.load(audioFiles[x])
    lenDifference = len(userAudio) - len(testAudio)
    print(lenDifference)
    if lenDifference > 0:
        print("User audio is bigger")
        for y in range(lenDifference):
            correlation = np.corrcoef(userAudio[y:len(testAudio)+y], testAudio)
            if correlation[1][0] > maxCorrelation:
                maxCorrelation = correlation[1][0]
                maxName = audioFiles[x].split("/")[2].split(".")[0].split("_")[0]
    elif lenDifference < 0:
        print("User test is bigger")
        for y in range(lenDifference):
            correlation = np.corrcoef(testAudio[y:len(userAudio)+y], userAudio)
            if correlation[1][0] > maxCorrelation:
                maxCorrelation = correlation[1][0]
                maxName = audioFiles[x].split("/")[2].split(".")[0].split("_")[0]
    else:
        print("Equal len")
        correlation = np.corrcoef(userAudio, testAudio)
        print(correlation[1][0])
        if correlation[1][0] > maxCorrelation:
            maxCorrelation = correlation[1][0]
            maxName = audioFiles[x].split("/")[2].split(".")[0].split("_")[0]
    print("------------------------------------")

    #print(len(testAudio))
print("Done!")
print(maxCorrelation)
print(maxName)

import sys
sys.path.insert(0, '../')

from emotionConnectionCalculator import *

ecc = emotionConnectionCalculator()

for i in range(0, 3):
	ecc.trainSent("happy", "happy")
	ecc.trainSent("sad", "sad")
	ecc.trainReceive("sad", "sad")


ecc.trainReceive("sad", "happy")
ecc.trainSent("happy", "sad")

assert(ecc.pGivenSent("happy", "happy") > ecc.pGivenSent("happy", "sad"))

assert(ecc.pGivenReceived("disgust", "content") == ecc.pGivenReceived("disgust", "wild"))
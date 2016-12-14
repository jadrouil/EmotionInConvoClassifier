from conversationExtract import *
import math

flatten = lambda orig, next: orig + next


class dataFolder:
	def __init__(self,filename,numfolds, emotions):
		convos = conversationExtract(filename, emotions)
		n = int(math.ceil(len(convos)/float(numfolds)))
		instanceFolds = [convos[i*n:i*n+n if i*n+n < len(convos) else len(convos)] for i in range(0, numfolds) ]
		self._rightFolds = instanceFolds[1:]
		self._leffFolds = []
		self._middle = instanceFolds[0]

	def train(self):
		return self._leffFolds + self._rightFolds
		
	def test(self):
		ret = self._middle
		self._leffFolds.append(self._middle)
		if self._rightFolds:
			self._middle = self._rightFolds[0]
			self._rightFolds = self._rightFolds[1:]
		else:
			self._middle = None

		return ret
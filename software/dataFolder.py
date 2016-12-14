from conversationExtract import *
import math

flatten = lambda orig, next: orig + next


class dataFolder:
	def __init__(self,filename,numfolds):
		convos = conversationExtract(filename)
		n = int(math.ceil(len(convos)/float(numfolds)))
		instanceFolds = [convos[i*n:i*n+n if i*n+n < len(convos) else len(convos)] for i in range(0, numfolds) ]
		self._rightFolds = instanceFolds
		self._leffFolds = []
		self._middle = None

	def train(self):
		return self._leffFolds + self._rightFolds
		
	def test(self):
		if not self._middle:
			ret = self._rightFolds[0]
			self._leffFolds = self._rightFolds[0]
			self._middle = self._leftFolds[1]
			self._rightFolds = self._rightFolds[2:]
		else:
			ret = self._middle
			self._left.append(self._middle)
			if self._right:
				self._middle = self._right[0]
				self._right = self._right[1:]
			else:
				self._middle = None

		return ret
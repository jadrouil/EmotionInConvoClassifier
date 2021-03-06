#Jeremy Drouillard jadrouil

from dataCollector import dataCollector
selectMaxProb = lambda current,new: current if current[1] > new[1] else new
class naiveBayeser:
	def __init__(self):
		self._dataCollector = dataCollector()

		
	def train(self, listOfInstances, weight = 1.0):
		for instance in listOfInstances:
			self._dataCollector.add(instance, weight)

	def test(self, instance, emotion):
		return self._dataCollector.calcProb(emotion, instance)


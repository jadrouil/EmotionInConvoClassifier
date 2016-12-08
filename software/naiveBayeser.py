#Jeremy Drouillard jadrouil

from dataCollector import dataCollector
selectMaxProb = lambda current,new: current if current[1] > new[1] else new
class naiveBayeser:
	def __init__(self):
		self._dataCollector = dataCollector()

	def _calculateProbabilities(self, instance):
		sensesAndProbability = [(sense, self._dataCollector.calcProb(sense, instance)) for sense in self._dataCollector.possibleSenses()]
		return sensesAndProbability

	def train(self, listOfInstances):
		for instance in listOfInstances:
			self._dataCollector.add(instance)

	def test(self, instance):
		sensesAndProbability = self._calculateProbabilities(instance)
		mostLikelyPrediction = reduce(selectMaxProb, sensesAndProbability, (None,None))
		assert(mostLikelyPrediction)
		return mostLikelyPrediction[0]


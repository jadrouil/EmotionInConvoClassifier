

class outputter:
	def __init__(self, fn):
		self._f = open(fn + ".out", "w+")
	def write(self, tags, convo):
		self._f.write("\n\n")
		assert(len(tags) == len(convo))
		for i in range(0, len(convo)):
			msg = convo[i]
			emo = tags[i]
			self._f.write("User" + str(msg.user()) + " " + emo + ": " + msg.content() + "\n")

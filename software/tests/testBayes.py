import sys
sys.path.insert(0, '../')

from naiveBayeser import *
from trainers import *
from naiveBayesInstance import *
nbc = naiveBayeser()

hotwordsTrain("hotwords", nbc)
tweetTrain("bayes", nbc, ["angry", "content"])
inst = instance("content", "word word word")
nbc.train([inst])

inst = instance("angry", "badword badword word")
nbc.train([inst])


inst = instance(None, "word and not")

assert(nbc.test(inst, "angry") < nbc.test(inst, "content"))
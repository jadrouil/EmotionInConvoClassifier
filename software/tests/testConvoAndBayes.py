import sys
sys.path.insert(0, '../')

from taggerFactory import *
from message import *


tagger = createConversationEmotionTagger("emotions", "conversations", "bayes", "hotwords")
convo = [message("blah blah blah", None, 1), message("wah wah wah", None, 2), message("bbb", None, 1), message("ccc", None, 2)]

print tagger.test(convo)
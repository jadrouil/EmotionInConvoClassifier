import sys
sys.path.insert(0, '../')

from taggerFactory import *


createConversationEmotionTagger("emotions", "conversations", "bayes", "hotwords")
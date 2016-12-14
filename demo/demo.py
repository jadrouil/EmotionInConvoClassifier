import os, sys
thisFileDir = os.path.dirname(__file__)
sys.path.append(os.path.join(thisFileDir, '../software'))

from message import message
from taggerFactory import createConversationEmotionTagger
from flask import Flask, render_template, request, current_app
import json

app = Flask(__name__)

tagger = createConversationEmotionTagger(
  emotionFile=sys.argv[1],
  conversationTrainfile=sys.argv[2],
  bayesTrainFile=sys.argv[3],
  hotwordsTrainFile=sys.argv[4]
)

@app.route("/")
def hello():
    return render_template('demo.html')

@app.route("/predict", methods=['POST'])
def predict():
    global tagger
    raw_conversation = request.get_json(force=True)
    conversation = []
    for c in raw_conversation:
        conversation.append(message(
            content=c['content'],
            eTag='',
            userId=c['userId'],
        ))

    prediction = tagger.test(conversation)

    return ', '.join(prediction)

if __name__ == "__main__":
    app.run(debug=1)

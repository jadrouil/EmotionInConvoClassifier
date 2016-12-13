import sys
sys.path.append('../software')

from message import message
from taggerFactory import createConversationEmotionTagger
from flask import Flask, render_template, request
import json

app = Flask(__name__)

@app.route("/")
def hello():
    return render_template('demo.html')

@app.route("/predict", methods=['POST'])
def predict():
    tagger = createConversationEmotionTagger(
      emotionFile='../datasets/emotions.txt',
      conversationTrainfile='../datasets/convo-train.json',
      bayesTrainFile='../datasets/tweets.csv',
      hotwordsTrainFile='../datasets/NRC-Emotion-Lexicon-v0.92/hotwords.txt',
    )


    raw_conversation = request.get_json(force=True)
    print 'poop'
    conversation = []
    for c in raw_conversation:
        conversation.append(message(
            content=c['content'],
            eTag=c['eTag'],
            userId=c['userId'],
        ))

    prediction = tagger.test(conversation)

    return ', '.join(prediction)

if __name__ == "__main__":
    app.run(debug=1)

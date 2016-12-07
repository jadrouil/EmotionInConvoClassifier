from flask import Flask, render_template, request
import json

app = Flask(__name__)

@app.route("/")
def hello():
    return render_template('demo.html')

@app.route("/predict", methods=['POST'])
def predict():
    conversation = request.get_json(force=True)

    # TODO: massage data

    # TODO: call external library
    prediction = 'happy'

    return prediction

if __name__ == "__main__":
    app.run(debug=1)

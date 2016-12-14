# Emotion Tagger
EECS 498 NLP Term Project<br>
mdobro@umich.edu, quincyd@umich.edu, jadrouil@umich.edu, mterwil@umich.edu

## Introduction
Use a modified Viterbi algorithm in combination with a Naive Bayes classifier
and a hotwords file to determine emotion in a conversation.

## Sample Usage
To test against the dataset in `datasets/convo-test.json`:

    $ make test

To cross-validate the algorithm on the dataset:
    $ make folds

To run the interactive demo:

    $ make demo


This will start a Python web server on port 5000.

## Software
- The main file for this algorithm is in taggerHandler.py
- The Viterbi portion of the algorithm is in ViterbiTable and ViterbiCell
- The probability calculators can be found in EmotionConnectionCalculator and EmotionMessageCalculator



## Notes
- Hotwords are weighted. Weight is determined by the first line in the hotwords
  file (datasets/hotwords.txt).
	-We encourage you to toggle the hotweight to see the affect it has on leabeling
- See the `datasets` folder for exmaples of how datasets should be formatted.
- Person 1 must speak first.
- Person 1 and 2 must alternate in the dialog.
- Conversations must be between exactly 2 people.

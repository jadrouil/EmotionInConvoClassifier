# Emotion Tagger
EECS 498 NLP Term Project
mdobro@umich.edu, quincyd@umich.edu, jadrouil@umich.edu, mterwil@umich.edu

## Introduction
Use a modified Viterbi algorithm in combination with a Naive Bayes classifier
and a hotwords file to determine emotion in a conversation.

## Sample Usage
To test against the dataset in `datasets/convo-test.json`:

    $ make test

To run the interactive demo:

    $ make demo

This will start a Python web server on port 5000.

## Notes
- Hotwords are weighted. Weight is determined by the first line in the hotwords
  file.
- See the `datasets` folder for exmaples of how datasets should be formatted.
- Person 1 must speak first.
- Person 1 and 2 must alternate in the dialog.
- Conversations must be between exactly 2 people.

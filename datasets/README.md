__`conversations-parsed`__ contains conversations parsed from
__`conversations-raw`__

__`convo-all.json`__ contains the sum of data from `conversations-parsed`

__`convo-test.json`__ and __`convo-train.json`__ are train and test data if you
are not folding

__`emotions.txt`__ is an emotion list for the system to take in

__`hotwords.txt`__ is a hotwords list with the hotwords weight in the first line
, which is an arbitrarily large integer 

__`tweets.csv`__ is used to train the Naive Bayes classifier

__`conversations-raw/conversations.txt`__ contains 36 raw conversations.

## Helpers

Use `conversations-raw/parseAndTagConversation.py` to parse and tag one of these
conversations.  Usage:

    $ ./parseAndTagConversations.py [conversation number]

After all conversations are parsed use
`conversations-parsed/joinConversations.py` to join them together into one data
file the project will accept. 

    $ ./joinConversations.py [max conversation id to join]

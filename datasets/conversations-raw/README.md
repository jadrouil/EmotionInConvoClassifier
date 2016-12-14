# Conversation Data

`conversations.txt` contains 36 raw conversations.

Use `parseAndTagConversation.py` to parse and tag one of these conversations.
Usage:

    $ ./parseAndTagConversations.py [conversation number]

After all conversations are parsed use `joinConversations.py` to join them
together into one data file the project will accept. You may want to refactor
this script to accept individual files to join rather than using a range for
more configurability. It is fairly straightfoward to modify to fit your needs.

    $ ./joinConversations.py [max conversation id to join]

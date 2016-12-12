#!/usr/bin/env python

from collections import OrderedDict
import sys
import json

with open(sys.argv[1]) as f:
    raw_conversations = f.read().split('\n\n')

with open(sys.argv[3]) as f:
    emotions = f.read().split('\n')
    emotions = [x.lower() for x in emotions if len(x) > 0]

start_index = input('There are {} conversations. Start index: '\
        .format(len(raw_conversations)))

stop_index = input('There are {} conversations. Stop index: '\
        .format(len(raw_conversations)))

with open(sys.argv[2], 'w') as outfile:
    conversations = []
    for i in range(start_index, stop_index):
        raw_messages = raw_conversations[i].split('\n')
        counter = 0
        messages = []
        for raw_message in raw_messages:
            if len(raw_message) <= 0:
                continue #garbage

            print ''
            print raw_message

            user, message    = raw_message.split(': ')
            user, message_id = user.split('.')

            # keep track of 'A.271' etc.
            counter += 1
            if counter != int(message_id):
                print('Warn: missed a message?')

            tag = None
            while True:
                ecounter = 0
                for e in emotions:
                    print '{}. {}'.format(ecounter, e)
                    ecounter += 1

                tag = input('Select: ')

                if tag < ecounter and tag >= 0:
                    tag = emotions[tag]
                    break


            messages.append({
              'user': user,
              'message_id': message_id,
              'message': message,
              'tag': tag,
            })

            conversations.append(messages)

        outfile.write(json.dumps(conversations))

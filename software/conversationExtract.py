import json

from message import message

def conversationExtract(conversationTrainfile, emotions):
    '''Extract conversations from a JSON file 

    Return: [[msg, ...], ...] nested list of conversations
    '''
    with open(conversationTrainfile) as trainfile:
        trainfile = json.loads(trainfile.read())

        conversations = []
        for conversation in trainfile:
            messages = []

            # default to B since A needs to come first
            lastUid = 2
            for raw_message in conversation['conversation']:
                if raw_message['tag'] not in emotions:
                    raise RuntimeError('Unseen emotion')

                if raw_message['user'] == 'A':
                    uid = 1
                elif raw_message['user'] == 'B':
                    uid = 2
                else:
                    raise RuntimeError('Bad uid')

                # if lastUid == 2:
                #     # next user should be 1
                #     assert(uid == 1)
                # else:
                #     # next user should be 2
                #     assert(uid == 2)

                lastUid = uid

                messages.append(message(
                  content=raw_message['message'],
                  eTag=raw_message['tag'],
                  userId=uid
                ))

            conversations.append(messages)
    return conversations

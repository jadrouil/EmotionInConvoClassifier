#!/usr/bin/env python

import json, sys

if len(sys.argv) != 2:
    print 'Usage: ./joinConversations.py [max conversation id]'
    exit(1)

with open('convo-combined.json', 'w') as f_combined:
    convos = []
    for i in range(int(sys.argv[1])):
        try:
            with open('convo-{i:02d}.json'.format(i=i)) as f_ind:
                convos.append({
                  'conversation_id': i,
                  'conversation': json.loads(f_ind.read())
                })
        except:
            print 'convo-{i:02d}.json could not be opened.  Skipping...'.format(i=i)

    f_combined.write(json.dumps(convos, indent=2))

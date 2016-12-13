#!/usr/bin/env python

import json, sys

with open('datasets/convo-combined.json', 'w') as f_combined:
    for i in range(int(sys.argv[1])):
        convos = []
        with open('datasets/convo-{}.json'.format(i)) as f_ind:
            convos.append({
              'conversation_id': i,
              'conversation': json.loads(f_ind.read())
            })

    f_combined.write(json.dumps(convos, indent=2))

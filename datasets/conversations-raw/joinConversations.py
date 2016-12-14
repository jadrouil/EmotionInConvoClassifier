#!/usr/bin/env python

import json, sys

with open('convo-combined.json', 'w') as f_combined:
    convos = []
    for i in range(int(sys.argv[1])):
        with open('convo-{}.json'.format(i)) as f_ind:
            convos.append({
              'conversation_id': i,
              'conversation': json.loads(f_ind.read())
            })

    f_combined.write(json.dumps(convos, indent=2))

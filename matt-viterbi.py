def viterbi(sentence):
    Score = {} # (tag, word pos)
    BP    = {} # back pointers

    # INITIALIZATION
    for t in T:
        Score[(t, 0)] = (emissions[(sentence[0][0], t)] * 1. / counts[t]) * (transitions[(BOS, t)] * 1. / bos_count)
        BP[(t, 0)]    = 0

    # ITERATION
    for w in range(1, len(sentence)):
        for t in T:
            tmp_score = (emissions[(sentence[w][0], t)] * 1. / counts[t])

            max_j     = None # j is a tag
            max_j_val = -1
            for j in T:
                val = Score[(j, w-1)] * (transitions[(j, t)] *1. / counts[j])
                if val > max_j_val:
                    max_j_val = val
                    max_j = j

            Score[(t, w)] = tmp_score * max_j_val * 1.
            BP[(t, w)]    = max_j

    # SEQUENCE ID
    Seq = [None] * len(sentence)

    # get options for the last word in the sentence
    last_word = [x for x in Score.keys() if x[1] == len(sentence) - 1]

    # and calculate the maximum
    max_score      = -1
    max_score_pair = None

    for i in last_word:
        if Score[i] > max_score:
            max_score      = Score[i]
            max_score_pair = i

    Seq[-1] = max_score_pair[0]

    for w in range(len(sentence) - 2, -1, -1):
        Seq[w] = BP[(Seq[w+1]), w+1]

    to_return = []
    for idx in range(len(sentence)):
        to_return.append((sentence[idx][0], Seq[idx]))

    return to_return

import unittest
from collections import defaultdict


def remeber_recall(inp):
    dictionary = defaultdict(set)
    for act_inp in inp[1:]:
        action, *inpt = act_inp
        if action == 1:
            synonyms = set(inpt)

            stored_syn = set()

            for word in synonyms:
                if word in dictionary:
                    stored_syn = dictionary[word]
                    break
            for word in synonyms:
                stored_syn.add(word)

            for word in inpt:
                dictionary[word] = stored_syn

        elif action == 2:
            query = list(inpt)[0]
            synonyms = [x for x in dictionary[query] if x != query]
            print(query + ": " + ",".join(sorted(synonyms)))




class SolutionTest(unittest.TestCase):

    def test_one(self):
        inp = [7,
               [1, 'good', 'sound', 'first-class'],
               [1, 'enough', 'abundant'],
               [1, 'adequate', 'enough', 'ample'],
               [2, 'adequate'],
               [2, 'good'],
               [1, 'bright', 'illuminous'],
               [2, 'cs']]
        remeber_recall(inp)

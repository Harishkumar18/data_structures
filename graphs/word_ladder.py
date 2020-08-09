"""https://bradfieldcs.com/algos/graphs/word-ladder/"""

from collections import defaultdict
from itertools import product
import os


def build_graph(words):
    buckets = defaultdict(list)
    graph = defaultdict(set)

    # we have a huge number of buckets, each of them with a four-letter word on the outside, except that one of the
    # letters in the label has been replaced by an underscore. For example we might have a bucket labeled “pop_.” As
    # we process each word in our list we compare the word with each bucket, using the ‘_’ as a wildcard,
    # so both “pope” and “pops” would match “pop_.” Every time we find a matching bucket, we put our word in that
    # bucket. Once we have all the words in the appropriate buckets we know that all the words in the bucket must be
    # connected.
    for word in words:
        for i in range(len(word)):
            bucket = '{}_{}'.format(word[:i], word[i+1:])
            # group on same buckets based in the key
            # {'_OOL': ['POOL', 'WOOL', 'FOOL']}
            buckets[bucket].append(word)

    # Add vertices and edgesfor words in the same bucket
    for bucket, mutual_neighbour in buckets.items():
        for word1, word2 in product(mutual_neighbour, repeat=2):
            if word1 != word2:
                graph[word1].add(word2)
                graph[word2].add(word1)

    return graph



vocabulary_words = ['POOL', 'WOOL', 'FOWL', 'FOAL', 'FOUL', 'FOOL', 'FOOD', 'FOLD', 'SOLD', 'SOLE', 'SALE']
word_graph = build_graph(vocabulary_words)
print(word_graph)
"""
Try to model the problem as a graph.
Since we're looking for the shortest transformation sequence,
we can use BFS.
"""
from collections import deque


def ladderLength(start, end, wordList):
    if end not in wordList:
        return 0

    wordList = set(wordList)
    wordList.add(start)
    q = deque([start])
    seen = {start}
    level = 1
    while q:
        for _ in range(len(q)):
            node = q.popleft()
            if node == end:
                return level

            for word in generate(node):
                if word not in seen and word in wordList:
                    seen.add(word)
                    q.append(word)
        level += 1

    return 0


def generate(word):
    res = set()
    for i in range(len(word)):
        for j in range(26):
            c = chr(97 + j)
            res.add(word[:i] + c + word[i + 1:])
    return res

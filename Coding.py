# Coding.py
import Library as Lib

WORDS = ["abcd", "dcba", "lls", "s", "sssll"]

trie = Lib.Trie()
for i, word in enumerate(WORDS):
    trie.insert(word)

result = []
for i, word in enumerate(WORDS):
    result.append(trie.search(word))

print(result)    


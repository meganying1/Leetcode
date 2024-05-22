# https://leetcode.com/problems/implement-trie-prefix-tree/
# difficulty: medium
# topics: hash table, string, design, trie

# problem:
# A trie (pronounced as "try") or prefix tree is a tree data structure used to efficiently store and retrieve keys in a dataset of strings. There are various applications of this data structure, such as autocomplete and spellchecker.
# Implement the Trie class:
#   Trie() Initializes the trie object.
#   void insert(String word) Inserts the string word into the trie.
#   boolean search(String word) Returns true if the string word is in the trie (i.e., was inserted before), and false otherwise.
#   boolean startsWith(String prefix) Returns true if there is a previously inserted string word that has the prefix prefix, and false otherwise.

class TrieNode:

    def __init__(self, letter):
        self.letter = letter
        self.nextLetters = {}

class Trie:

    def __init__(self):
        self.trie = TrieNode(None)

    def insert(self, word: str) -> None:
        curr = self.trie
        for c in word:
            currLetters = curr.nextLetters
            if c not in currLetters:
                currLetters[c] = TrieNode(c)
            curr = currLetters[c]
        curr.nextLetters[None] = None

    def search(self, word: str) -> bool:
        curr = self.trie
        for c in word:
            currLetters = curr.nextLetters
            if c not in currLetters: return False
            curr = currLetters[c]
        if None in curr.nextLetters: return True
        return False

    def startsWith(self, prefix: str) -> bool:
        curr = self.trie
        for c in prefix:
            currLetters = curr.nextLetters
            if c not in currLetters: return False
            curr = currLetters[c]
        return True

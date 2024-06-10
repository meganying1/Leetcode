# https://leetcode.com/problems/replace-words/
# difficulty: medium
# topics: array, hash table, string, trie

# problem:
# In English, we have a concept called root, which can be followed by some other word to form another longer word - let's call this word derivative. For example, when the root "help" is followed by the word "ful", we can form a derivative "helpful".
# Given a dictionary consisting of many roots and a sentence consisting of words separated by spaces, replace all the derivatives in the sentence with the root forming it. If a derivative can be replaced by more than one root, replace it with the root that has the shortest length.
# Return the sentence after the replacement.

class TrieNode:
    def __init__(self, c):
        self.c = c
        self.next = {}
    
class Trie:
    def __init__(self):
        self.trie = TrieNode(None)
    def insert(self, s):
        curr = self.trie
        for c in s:
            if c not in curr.next: curr.next[c] = TrieNode(c)
            curr = curr.next[c]
        curr.next[None] = None
    def getRoot(self, s):
        ans = []
        curr = self.trie
        for c in s:
            if c in curr.next: ans.append(c)
            else: return s
            curr = curr.next[c]
            if None in curr.next: break
        return "".join(ans)

class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        trie = Trie()
        ans = []
        for s in dictionary:
            trie.insert(s)
        for s in sentence.split(" "):
            ans.append(trie.getRoot(s))
        return " ".join(ans)
# time complexity: O(d*w + s*w)
#   d is number of words in dictionary, s is number of words in sentence, and w is average length of word in dictionary
#   to insert all strings of dictionary into trie: O(d * w)
#   to replace all strings in sentence with their roots: O (s * w)
# space complexity: O(d*w + s*w)

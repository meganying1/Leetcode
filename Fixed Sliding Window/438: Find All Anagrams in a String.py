# https://leetcode.com/problems/find-all-anagrams-in-a-string/description/
# difficulty: medium
# topics: hash table, string, sliding window

# problem:
# Given two strings s and p, return an array of all the start indices of p's anagrams in s. You may return the answer in any order.
# An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        pLength, sLength = len(p), len(s)
        if pLength > sLength: return []
        ans, pHash = [], 1
        valMap = {'a': 2, 'b': 3, 'c': 5, 'd': 7, 'e': 11, 'f': 13, 'g': 17, 'h': 19, 'i': 23, 'j': 29, 'k': 31, 'l': 37, 'm': 41, 'n': 43, 'o': 47, 'p': 53, 'q': 59, 'r': 61, 's': 67, 't': 71, 'u': 73, 'v': 79, 'w': 83, 'x': 89, 'y': 97, 'z': 101}
        for c in p: pHash *= valMap[c]
        start, end = 0, pLength-1
        currHash = 1
        for i in range(pLength): currHash *= valMap[s[i]]
        while end < sLength:
            if currHash == pHash: ans.append(start)
            end += 1
            if end == sLength: break
            currHash = (currHash // valMap[s[start]]) * valMap[s[end]]
            start += 1
        return ans

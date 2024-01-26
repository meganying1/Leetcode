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

        def areAnagrams(sCounts, pCounts):
            for c in pCounts:
                if pCounts[c] != sCounts[c]: return False
            return True
            
        pCounts, sCounts = defaultdict(int), defaultdict(int)
        start, end = 0, pLength-1
        for c in p: pCounts[c] += 1
        for i in range(pLength): sCounts[s[i]] += 1
        ans = [0] if areAnagrams(sCounts, pCounts) else []
        while end < sLength-1:
            sCounts[s[start]] -= 1
            sCounts[s[end+1]] += 1
            start += 1
            end += 1
            if areAnagrams(sCounts, pCounts): ans.append(start)
        return ans

        return ans
# time complexity: O(26n)
#     time to check if two strings are anagrams is based on number of unique letters
# if there are huge amount of letters, counts may become very large and comparisons will take a lot of time
#     but rate at which those counts grow is much slower than rate at which product of prime values grow

"""
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
"""
# time complexity: O(n*t), where t is amount of time it the math takes
# numbers can get really, really big: we cannot assume solution to be constant time

# https://leetcode.com/problems/word-break/description/
# difficulty: medium
# topics: array, hash table, string, dynamic programming, trie, memoization

# program:
# Given a string s and a dictionary of strings wordDict, return true if s can be segmented into a space-separated sequence of one or more dictionary words.
# Note that the same word in the dictionary may be reused multiple times in the segmentation.

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        mod = (10**9) + 7
        n = len(s)
        cache = [None] * (n+1)

        def getVal(c):
            return ord(c)-ord('a')+1
        
        def getHash(s):
            ans = 0
            for c in s: ans = ((ans * 26) + getVal(c)) % mod
            return ans
            
        hashDict = defaultdict(set)
        for word in wordDict: hashDict[getHash(word)].add(word)

        def dp(start):
            if start == n: return True
            if cache[start] != None: return cache[start]
            hashVal = 0
            end = start
            while end < n:
                hashVal = ((hashVal * 26) + getVal(s[end])) % mod
                if hashVal in hashDict and s[start:end+1] in hashDict[hashVal]:
                    ans = dp(end+1)
                    cache[start] = ans
                    if ans == True: return True
                end += 1
            cache[start] = False
            return False

        return dp(0)

# top-down with memoization
# time complexity: O(len(s)^2) + O(total chars in wordDict)
#     while loop and substring check each take n time
#     O(len(wordDict) * (average length of word in wordDict)) = O(total chars in wordDict)
# space complexity: O(total chars in wordDict) + O(len(s))
#     we require O(len(s)) space for cache

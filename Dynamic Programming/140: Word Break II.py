# https://leetcode.com/problems/word-break-ii/
# difficulty: hard
# topics: array, hash table, string, dynamic programming, backtracking, trie, memoization

# problem:
# Given a string s and a dictionary of strings wordDict, add spaces in s to construct a sentence where each word is a valid dictionary word. Return all such possible sentences in any order.
# Note that the same word in the dictionary may be reused multiple times in the segmentation.

# dp with memoization
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        n = len(s)
        wordSet = set(wordDict)
        cache = {}

        def dp(start):
            if start in cache: return cache[start]
            result = []
            if start == n: return [[]]
            for end in range(start+1, n+1):
                word = s[start:end]
                if word in wordSet:
                    for nextWord in dp(end): result.append([word] + nextWord)
            cache[start] = result
            return result
        
        ans = dp(0)
        return [" ".join(word) for word in ans]
# time complexity: O(n^2 * 2^n)
  # size of tree is 2^n
  # while loop and string slicing take O(n) time
# space complexity: O(n * 2^n)
  # each possible result takes O(n) space

# naive backtracking
"""
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        ans = []
        n = len(s)
        wordSet = set(wordDict)

        def backtrack(start, currSentence):
            if start == n:
                ans.append(" ".join(currSentence))
                return
            for end in range(start+1, n+1):
                word = s[start:end]
                if word in wordSet:
                    currSentence.append(word)
                    backtrack(end, currSentence)
                    currSentence.pop()
        
        backtrack(0, [])
        return ans
"""

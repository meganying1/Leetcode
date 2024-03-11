# https://leetcode.com/problems/longest-palindromic-substring/description/
# difficulty: medium
# topics: string, dynamic programming

# problem:
# Given a string s, return the longest palindromic substring in s.

class Solution:
    def longestPalindrome(self, s: str) -> str:
        length = len(s)
        self.maxLen = 0
        self.ans = ""
        
        def checkPal(start, end):
            while start >= 0 and end < length and s[start] == s[end]:
                if (end-start+1) > self.maxLen:
                    self.maxLen = end-start+1
                    self.ans = s[start:end+1]
                start -= 1
                end += 1
    
        for i in range(length):
            checkPal(i, i)
            checkPal(i, i+1)
        return self.ans

"""
class Solution:
    def longestPalindrome(self, s: str) -> str:
        length = len(s)
        cache = [[None] * (length+1) for i in range(length+1)]
        
        def dp(start, end):
            if start >= end: return True
            if cache[start][end] != None: return cache[start][end]
            if dp(start+1, end-1) and s[start] == s[end]: cache[start][end] = True
            else: cache[start][end] = False
            return cache[start][end]
        
        maxLen = 0
        ans = ""
        for start in range(length):
            for end in range(length-1, start-1, -1):
                if dp(start, end) and (end-start+1) > maxLen:
                    maxLen = end-start+1
                    ans = s[start:end+1]
        return ans
"""

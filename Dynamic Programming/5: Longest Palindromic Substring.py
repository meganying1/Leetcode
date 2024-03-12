# https://leetcode.com/problems/longest-palindromic-substring/description/
# difficulty: medium
# topics: string, dynamic programming

# problem:
# Given a string s, return the longest palindromic substring in s.

class Solution:
    def longestPalindrome(self, s: str) -> str:
        length = len(s)
        ansStart = 0
        ansEnd = 0
        
        def checkPal(start, end):
            nonlocal ansStart
            nonlocal ansEnd
            while start >= 0 and end < length and s[start] == s[end]:
                if (end-start+1) > (ansEnd-ansStart+1):
                    ansStart, ansEnd = start, end
                start -= 1
                end += 1
    
        for i in range(length):
            checkPal(i, i)
            checkPal(i, i+1)
        return s[ansStart:ansEnd+1]

"""
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
# bottom-up
# time complexity: O(n^3)
#     for loop takes O(n) time, while loop takes O(n) time, and substring call takes O(n) time

# avoid using class variables like self.ans
#     class variables are for when you have an object that requires a persistent state 

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
# top-down
# time complexity: O(n^3)
#     double nested for loop takes O(n^2) time and substring call s[start:end+1] takes O(n) time
#     can save time by storing answer as start and end points rather than string
# space complexity: O(n^2)
#     wasting a lot of space because we don't care about certain start and end pairs (for example, start = 10 and end = 5)
#     consider using {} cache instead, and store (start, end) pairs

# good practice to loop through all start and end pairs in dp function

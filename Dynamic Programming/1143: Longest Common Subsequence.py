# https://leetcode.com/problems/longest-common-subsequence/description/
# difficulty: medium
# topics: string, dynamic programming

# problem:
# Given two strings text1 and text2, return the length of their longest common subsequence. If there is no common subsequence, return 0.
# A subsequence of a string is a new string generated from the original string with some characters (can be none) deleted without changing the relative order of the remaining characters.
#   For example, "ace" is a subsequence of "abcde".
# A common subsequence of two strings is a subsequence that is common to both strings.

class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        len1, len2 = len(text1), len(text2)
        cache = {}
        
        def dp(i, j):
            if i < 0 or j < 0: return 0
            if (i, j) in cache: return cache[(i, j)]
            if text1[i] == text2[j]: return 1 + dp(i-1, j-1)
            ans = max(dp(i-1, j), dp(i, j-1))
            cache[(i, j)] = ans
            return ans

        return dp(len1-1, len2-1)
# top-down + memoization
# time complexity: O(n*m)
# space complexity: O(n*m)

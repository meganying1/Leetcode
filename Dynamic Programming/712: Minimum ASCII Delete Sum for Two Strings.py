# https://leetcode.com/problems/minimum-ascii-delete-sum-for-two-strings/
# difficulty: medium
# topics: array, dynamic programming

# description:
# Given two strings s1 and s2, return the lowest ASCII sum of deleted characters to make two strings equal.

class Solution:
    def minimumDeleteSum(self, s1: str, s2: str) -> int:
        n, m = len(s1), len(s2)
        dp = [[0] * (m+1) for _ in range(n+1)]
        for i in range(n):
            for j in range(m):
                if s1[i] == s2[j]: dp[i+1][j+1] = dp[i][j] + ord(s1[i])
                else: dp[i+1][j+1] = max(dp[i][j+1], dp[i+1][j])
        total = sum(ord(c) for c in s1) + sum(ord(c) for c in s2)
        return total - 2 * dp[n][m]
# we want to minimize the sum of ascii values of characters that we delete, which means we want to maximixe the sum of ascii values of characters we keep
# dp[i][j] represents the sum of ascii values of characters we keep from s1[:i+1] and s2[:j+1]
# if s1[i] = s2[j], then we have the same character and we want to keep it
# if s1[i] != s2[j], then we have to skip one of the charcters
#   if we skip s1[i], the sum of ascii values of characters that we keep is equal to dp[i-1][j]
#   if we skip s2[j], the sum of ascii values of characters that we keep is equal to dp[i][j-1]
#   we choose the option that maximizes the sum
# the final answer is equal to the sum of ascii values of all the characters in both strings minus the sum of ascii values we keep

# time complexity: O(n*m)
# space complexity: O(n*m)

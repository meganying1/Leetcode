# https://leetcode.com/problems/longest-binary-subsequence-less-than-or-equal-to-k/
# topics: array, dynamic programming, greedy, memoization
# difficulty: medium

# You are given a binary string s and a positive integer k.
# Return the length of the longest subsequence of s that makes up a binary number less than or equal to k.
# Note:
#   The subsequence can contain leading zeroes.
#   The empty string is considered to be equal to 0.
# A subsequence is a string that can be derived from another string by deleting some or no characters without changing the order of the remaining characters.

class Solution:
    def longestSubsequence(self, s: str, k: int) -> int:
        ans, currVal = s.count('0'), 0
        n = len(s)
        for i in range(n-1, -1, -1):
            if s[i] == '1':
                currVal += 2 ** (n-i-1)
                if currVal <= k: ans += 1
                else: break
        return ans
# time complexity: O(n)
# space complexity: O(1)

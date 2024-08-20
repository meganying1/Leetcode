# https://leetcode.com/problems/2-keys-keyboard
# difficulty: medium
# topics: math, dynamic progarmming

# problem:
# There is only one character 'A' on the screen of a notepad. You can perform one of two operations on this notepad for each step:
#   Copy All: You can copy all the characters present on the screen (a partial copy is not allowed).
#   Paste: You can paste the characters which are copied last time.
# Given an integer n, return the minimum number of operations to get the character 'A' exactly n times on the screen.

class Solution(object):
    def minSteps(self, n):
        if n == 1: return 0
        cache = {}
        
        def dp(currLen, pasteLen):
            if currLen == n: return 0
            if currLen > n: return float("inf")
            if (currLen, pasteLen) in cache: return cache[(currLen, pasteLen)]
            ans = min(dp(currLen*2, currLen) + 2, dp(currLen+pasteLen, pasteLen) + 1)
            cache[(currLen, pasteLen)] = ans
            return ans

        return dp(1, 1) + 1
# base cases:
#     if we successfully reach a length of n A's, return 0
#     if we have length greater than n A's, return infinity to ignore this sequence
# subproblems:
#     try copying all and then pasting, which takes two operations: currLen doubles and pasteLen becomes currLen
#     try pasting, which takes one operation: add pasteLen to currLen and pasteLen stays the same
        
# time complexity: O(n^2)
# space complexity: O(n^2)

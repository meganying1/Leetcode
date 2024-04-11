# https://leetcode.com/problems/unique-binary-search-trees/description/
# difficulty: medium
# topics: math, dynamic programming, tree, binary search tree, binary tree

# problem:
# Given an integer n, return the number of structurally unique BST's (binary search trees) which has exactly n nodes of unique values from 1 to n.

class Solution:
    def numTrees(self, n: int) -> int:
        cache = [None] * (n+1)

        def dp(num):
            if num == 0 or num == 1: return 1
            if cache[num] != None: return cache[num]
            ans = 0
            for i in range(num): ans += dp(i) * dp(num-i-1)
            cache[num] = ans
            return ans
        
        return dp(n)

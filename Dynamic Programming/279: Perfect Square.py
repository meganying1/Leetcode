# https://leetcode.com/problems/perfect-squares/description/
# difficulty: medium
# topics: math, dynamic programming, breadth-first search

class Solution:
    def numSquares(self, n: int) -> int:
        cache = [float('inf')] * (n+1)
        def dp(num):
            if math.sqrt(num) == math.floor(math.sqrt(num)): return 1
            if cache[num] != float('inf'): return cache[num]
            for val in range(math.floor(math.sqrt(num)), 0, -1):
                newNum = num - val**2
                cache[num] = min(dp(newNum) + 1, cache[num])
            return cache[num]
        return dp(n)
# time complexity: O(n*root(n))
#   there are n possible states (as defined by the parameters of your dp function / as defined by your cache)
#   each state takes root(n) time
# space complexity: O(n)

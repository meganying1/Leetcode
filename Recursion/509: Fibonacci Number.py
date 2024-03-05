# https://leetcode.com/problems/fibonacci-number/description/
# difficulty: easy
# topics: math, dynamic programming, recursion, memoization

# problem:
# The Fibonacci numbers, commonly denoted F(n) form a sequence, called the Fibonacci sequence, such that each number is the sum of the two preceding ones, starting from 0 and 1. That is,
#   F(0) = 0, F(1) = 1
#   F(n) = F(n - 1) + F(n - 2), for n > 1.
# Given n, calculate F(n).

"""
class Solution:
    def fib(self, n: int) -> int:
        if n == 0 or n == 1: return n
        return self.fib(n-1) + self.fib(n-2)
"""
# uses recursion, which is very slow
# time complexity: O(2^n)
#   base case is first or second fibonacci number
#   time complexity for a single call to fib() is constant assumign we have the child values already
#   generally speaking in recursion, time complexity of code = (number of recursive calls) * (amount of time each recursive call takes
#     if you represent each call to the fib function as a node, there are 2^n nodes because depth of the tree is n and the branching factor is 2^n; so number of calls to the fib function is 2^n calls
#     technically branching factor isn't exactly two because we're not doing fib(n) = fib(n-1) + fib(n-1), true complexity is (golden ratio)^n

# space complexity: O(n)
# recursive callstack uses space, and each of those callstacks takes constant space, because there's a constant amount of variables inside a single call to fib()
# each node takes O(1) space, but the space complexity is not 2^n because not all calls/callstacks exist at the same time
#   for example, say we start at fib(5)
#     before computeing f(4), we need to compute f(3) and descend down to f(1)
#     now f(2) can resume running
#   maximum depth of the callstack at any given time is n becuase you start at the root, snake all the way down, compute the lowest value, pop back up a bit, go down again, go up a bit, etc.
# since we have at most n calls on the callstack and each callstack takes O(1) space, the space complexity is O(n)

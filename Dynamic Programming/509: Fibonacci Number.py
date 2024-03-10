# https://leetcode.com/problems/fibonacci-number/description/
# difficulty: easy
# topics: math, dynamic programming, recursion, memoization

# problem:
# The Fibonacci numbers, commonly denoted F(n) form a sequence, called the Fibonacci sequence, such that each number is the sum of the two preceding ones, starting from 0 and 1. That is,
#   F(0) = 0, F(1) = 1
#   F(n) = F(n - 1) + F(n - 2), for n > 1.
# Given n, calculate F(n).

class Solution:
    def fib(self, n: int) -> int:
        if n == 0: return 0
        prev, prev2 = 1, 0
        for i in range(2, n+1):
            prev = prev + prev2
            prev2 = prev - prev2
        return prev
# space-optimized tabluation:
#     can optimize space by overwriting part of cache continuously
#     typically cannot optimize time
#     not possible with bottom-up memoization because of its recursive nature
# time complexity: O(n)
# space complexity: O(1)

# in general for DP:
#     space = size of cache
#     time = size of cache * time per cache call
# usually easy to know when to use dp or not 
#     many problems are: “you can do 1 of these 2 options over and over, what is the max score you can get?”

"""
class Solution:
    def fib(self, n: int) -> int:
        if n == 0: return 0
        dp = [0 for i in range(n+1)]
        dp[1] = 1
        for i in range(2, n+1):
            dp[i] = dp[i-1] + dp[i-2]
        return dp[-1]
"""
# can be further optimized because not all values need to be stored in dp array: only values that matter are two previous values
# tabulation:
#     we have to define the order in which we solve the problem, so we start at the base cases, and build up
#     that seems simple, but in many problems the “order” we fill out the cache table becomes more complex, often requiring jumping around various parts of the table
#     more performant because there isn’t recursive overhead: recursion is usually quite expensive
#     one significant benefit to bottom-up tabulation that top-down memoization cannot do: can often optimize space complexity 
# time complexity: O(n)
#     table takes n time to fill out
#     for loop also takes n time
# space complexity: O(n)
#     table requires n space

"""
class Solution:
    def fib(self, n: int) -> int:
        cache = [None] * (n+1)
        def dp(num):
            if num <= 1: return num
            if cache[num] != None: return cache[num]
            res = dp(num-1) + dp(num-2)
            cache[num] = res
            return res
        return dp(n)
"""
# memoization + recursion: considered “top-down” because it works by thinking of the big problem we want to solve
#     easier than "bottom-up" tabulation because we don't know the order the cache gets filled
#     bottom-up tabulation is generally more performant CPU-wise, though harder, because you have to know the order to fill the cache table as well
#     should use top-down for 95% of DP problems
# time complexity: O(n)
#     for DP, to claculate time: (# of possible states) * (time each state takes)
#     each state here takes constant time and we have n states
# space complexity: O(n)
#     space complexity usually equals size of cache
#     we store at most n results in our cache, meaning we need n space
#     the callstack also uses n space, but the cache dominates the callstack always

"""
class Solution:
    def helper(self, n, cache):
        if n in cache: return cache[n]
        if n == 0: ans = 0
        elif n == 1: ans = 1
        else: ans = self.helper(n-1, cache) + self.helper(n-2, cache)
        cache[n] = ans
        return ans

    def fib(self, n: int) -> int:
        return self.helper(n, {})
"""
# should define helper function inside fib() function: the helper function is only ever needed inside the fib function anyway
# {} vs. []:
#     great thing about {} is it doesn’t store values that aren’t needed
#     if you use [] cache, you need to first fill it with dummy values, meaning no matter how cache is used, you always use n storage, because I first store None everywhere
#     in some problems, not every value in the cache gets filled, so I could be more efficient by using {}, which doesn’t require pre-allocating an array of a certain size
#     in the fib problem, we necessarily fill all values of the cache, because to solve fib(10), we always need to solve fib(9), fib(8), etc.
#     in general, using {} can be better if we get to “skip” filling out some values in the cache- because [] requires pre-allocating the array
#     here in the fib problem, we never get to skip values, so both {} and [] always use exactly n memory
#     arrays are more performant than hashmaps, so better to use [] here

"""
class Solution:
    def fib(self, n: int) -> int:
        if n == 0 or n == 1: return n
        return self.fib(n-1) + self.fib(n-2)
"""
# recursion:
# time complexity: O(2^n)
#     base case is first or second fibonacci number
#     time complexity for a single call to fib() is constant assuming we have the child values already
#     generally speaking in recursion, time complexity of code = (number of recursive calls) * (amount of time each recursive call takes
#         if you represent each call to the fib function as a node, there are 2^n nodes because depth of the tree is n and the branching factor is 2^n; so number of calls to the fib function is 2^n calls
#         technically branching factor isn't exactly two because we're not doing fib(n) = fib(n-1) + fib(n-1), true complexity is (golden ratio)^n
# space complexity: O(n)
#     recursive callstack uses space, and each of those callstacks takes constant space, because there's a constant amount of variables inside a single call to fib()
#     each node takes O(1) space, but the space complexity is not 2^n because not all calls/callstacks exist at the same time
#         for example, say we start at fib(5)
#         before computeing f(4), we need to compute f(3) and descend down to f(1)
#         now f(2) can resume running
#     maximum depth of the callstack at any given time is n becuase you start at the root, snake all the way down, compute the lowest value, pop back up a bit, go down again, go up a bit, etc.
#     since we have at most n calls on the callstack and each callstack takes O(1) space, the space complexity is O(n)

# https://leetcode.com/problems/count-good-numbers/
# topics: math, recursion
# difficulty: medium

# problem:
# A digit string is good if the digits (0-indexed) at even indices are even and the digits at odd indices are prime (2, 3, 5, or 7).
#   For example, "2582" is good because the digits (2 and 8) at even positions are even and the digits (5 and 2) at odd positions are prime. However, "3245" is not good because 3 is at an even index but is not even.
# Given an integer n, return the total number of good digit strings of length n. Since the answer may be large, return it modulo 109 + 7.
# A digit string is a string consisting of digits 0 through 9 that may contain leading zeros.

class Solution:
    def countGoodNumbers(self, n: int) -> int:
        evens, odds = n//2 + n%2, n//2
        mod = 10 ** 9 + 7

        def binPow(a, b):
            ans = 1
            while b > 0:
                if b & 1: ans = (ans * a) % mod
                a = (a * a) % mod
                b //= 2
            return ans

        return (binPow(5, evens) * binPow(4, odds)) % (10 ** 9 + 7)
# time complexity: O(logn)
# space complexity: O(n)

# our solution uses binary exponentiation to calculate a^n in O(logn) time rather than O(n) time
#   idea is that if n is even, we can express a^n as (a^(n/2))^2, and if n is odd, we can express a^n as a*(a^((n-1)/2))^2
#   we compute log(n) powers of a and do at most log(n) multiplications

"""
class Solution:
    def countGoodNumbers(self, n: int) -> int:
        evens, odds = n//2 + n%2, n//2
        return ((5 ** evens) * (4 ** odds)) % (10 ** 9 + 7)
"""
# time complexity: O(n)
#    we compute n multiplications
# space complexity: O(1)

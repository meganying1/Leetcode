# https://leetcode.com/problems/number-of-steps-to-reduce-a-number-in-binary-representation-to-one/
# difficulty: medium
# topics: math, bit manipulation, simulation

# description: 
# Given an integer n, return the decimal value of the binary string formed by concatenating the binary representations of 1 to n in order, modulo 109 + 7.

class Solution:
    def concatenatedBinary(self, n: int) -> int:
        ans = 0
        mod = 10 ** 9 + 7
        for i in range(1, n+1):
            bits = i.bit_length()
            ans <<= bits
            ans = (ans + i) % mod
        return ans
# time complexity: O(n)
# space complexity: O(1)

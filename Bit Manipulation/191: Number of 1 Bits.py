# https://leetcode.com/problems/number-of-1-bits/
# difficulty: easy
# topics: divide and conquer, bit manipulation

# problem:
# Write a function that takes the binary representation of a positive integer and returns the number of set bits it has (also known as the Hamming weight).

class Solution:
    def hammingWeight(self, n: int) -> int:
        ans = 0
        while n > 0:
            ans += n & 1
            n >>= 1
        return ans
# time complexity: O(k)
#   k is the number of bits in n
# space complexity: O(1)

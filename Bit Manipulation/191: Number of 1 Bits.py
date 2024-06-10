# https://leetcode.com/problems/number-of-1-bits/
# difficulty: easy
# topics: divide and conquer, bit manipulation

# problem:
# Write a function that takes the binary representation of a positive integer and returns the number of set bits it has (also known as the Hamming weight).

class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0
        while n:
            count += n & 1
            n >>= 1
        return count
# time complexity: O(logn)
# space complexity: O(1)

"""
class Solution:
    def hammingWeight(self, n: int) -> int:
        ans = 0
        while n > 0:
            ans += n & 1
            n >>= 1
        return ans
"""
# time complexity: O(k)
#   k is the number of bits in n
# space complexity: O(1)

# need to think about how while loop works: for the computer to check if a number is not 0, it has to check if any of the bits are set
#     assuming n is a 32-bit integer, the machine has to do a scan of all 32 bits every time it needs to check if n is > 0 
#     so the while loop takes O(32) to run one iteration in a way, but we already know that our number has say 32 bits at most
# instead we can do: for offset in range(32): (check if the offset-th bit is set, and if so add 1 to the result)
#     in practice doesn't matter since bit operations are very very quick

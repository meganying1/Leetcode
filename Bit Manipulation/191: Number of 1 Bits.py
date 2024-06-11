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
#     if we treat while loop as O(logn) time and bit operations as O(1) time (what most people would say)
#     need to explain to interviewer
#         could also argue that while loop is O(32) -> O(1) time and therefore entire solution is constant
#         could also argue that if n is very large, bit operations can take O(logn) time -> overall time complexity would be O(log^2 n)
#         could even argue the time complexity is O(log^3 n), O(logn) for the while loop, O(logn) for the creation of a number in the loop, and O(logn) for the bit operations
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
# time complexity: O(logn)
#     see time complexity from above
# space complexity: O(1)

# need to think about how while loop works: for the computer to check if a number is not 0, it has to check if any of the bits are set
#     assuming n is a 32-bit integer, the machine has to do a scan of all 32 bits every time it needs to check if n is > 0 
#     so the while loop takes O(32) to run one iteration in a way, but we already know that our number has say 32 bits at most
# instead we can do: for offset in range(32): (check if the offset-th bit is set, and if so add 1 to the result)
#     in practice doesn't matter since bit operations are very very quick
# think of any sort of operation on an integer as O(32) time

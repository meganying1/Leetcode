# https://leetcode.com/problems/single-number/
# difficulty: easy
# topics: array bit manipulation

# problem:
# Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.
# You must implement a solution with a linear runtime complexity and use only constant extra space.

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        xor = 0
        for n in nums: xor ^= n
        return xor
# time complexity: O(n)
# space complexity: O(1)

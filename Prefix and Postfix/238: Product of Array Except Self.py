# https://leetcode.com/problems/product-of-array-except-self/description/
# difficulty: medium
# topics: array, prefix sum

# problem:
# Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].
# The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
# You must write an algorithm that runs in O(n) time and without using the division operation.

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        length = len(nums)
        ans = [0] * length
        left, right = 1, 1
        for i in range(length):
            ans[i] = left
            left *= nums[i]
        for i in range(length-1, -1, -1):
            ans[i] *= right
            right *= nums[i]
        return ans

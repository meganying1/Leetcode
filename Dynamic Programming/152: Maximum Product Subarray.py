# https://leetcode.com/problems/maximum-product-subarray/description/
# difficulty: medium
# topics: array, dynamic programming

# problem:
# Given an integer array nums, find a subarray that has the largest product, and return the product.
# The test cases are generated so that the answer will fit in a 32-bit integer.

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1: return nums[0]
        ans = maxVal = minVal = nums[0]
        for i in range(1, n):
            curr = nums[i]
            if curr < 0: maxVal, minVal = minVal, maxVal
            maxVal = max(curr, curr * maxVal)
            minVal = min(curr, curr * minVal)
            ans = max(ans, maxVal)
        return ans
# space-optimized bottom-up
# time complexity: O(n)
# space complexity: O(1)

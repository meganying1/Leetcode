# https://leetcode.com/problems/maximum-value-of-an-ordered-triplet-i/
# difficulty: easy
# topics: array

# problem:
# You are given a 0-indexed integer array nums.
# Return the maximum value over all triplets of indices (i, j, k) such that i < j < k. If all such triplets have a negative value, return 0.
# The value of a triplet of indices (i, j, k) is equal to (nums[i] - nums[j]) * nums[k].

# greedy solution
class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        if max(nums) <= 0: return 0
        n = len(nums)
        currMax = maxDiff = ans = 0
        for k in range(n):
            ans = max(ans, maxDiff * nums[k])
            currMax = max(currMax, nums[k])
            maxDiff = max(maxDiff, currMax - nums[k])
        return ans
# time complexity: O(n)
# space complexity: O(1)

# prefix + postfix solution
class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        if max(nums) <= 0: return 0
        n = len(nums)
        prefixMax, postfixMax = [0] * n, [0] * n
        ans = 0
        for i in range(1, n):
            prefixMax[i] = max(prefixMax[i-1], nums[i-1])
            postfixMax[n-i-1] = max(postfixMax[n-i], nums[n-i])
        for j in range(1, n-1):
            ans = max(ans, (prefixMax[j]-nums[j]) * postfixMax[j])
        return ans
# time complexity: O(n)
# space complexity: O(n)

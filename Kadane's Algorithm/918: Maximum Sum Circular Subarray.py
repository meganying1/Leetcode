# https://leetcode.com/problems/maximum-sum-circular-subarray/description/
# difficulty: medium
# topics: array, divide and conquer, dynamic programming, queue, monotonic queue

# problem:
# Given a circular integer array nums of length n, return the maximum possible sum of a non-empty subarray of nums.
# A circular array means the end of the array connects to the beginning of the array. Formally, the next element of nums[i] is nums[(i + 1) % n] and the previous element of nums[i] is nums[(i - 1 + n) % n].
# A subarray may only include each element of the fixed buffer nums at most once. Formally, for a subarray nums[i], nums[i + 1], ..., nums[j], there does not exist i <= k1, k2 <= j with k1 % n == k2 % n.

class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        length = len(nums)
        currMaxSum, currMinSum, totalSum = nums[0], nums[0], nums[0]
        maxSum, minSum = nums[0], nums[0]
        for i in range(1, length):
            totalSum += nums[i]
            currMaxSum = max(nums[i], currMaxSum+nums[i])
            currMinSum = min(nums[i], currMinSum+nums[i])
            maxSum = max(maxSum, currMaxSum)
            minSum = min(minSum, currMinSum)
        return max(maxSum, totalSum-minSum) if totalSum != minSum else maxSum

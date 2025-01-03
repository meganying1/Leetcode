# https://leetcode.com/problems/number-of-ways-to-split-array/
# difficulty: medium
# topics: array, prefix sum

# problem:
# You are given a 0-indexed integer array nums of length n.
# nums contains a valid split at index i if the following are true:
#   The sum of the first i + 1 elements is greater than or equal to the sum of the last n - i - 1 elements.
#   There is at least one element to the right of i. That is, 0 <= i < n - 1.
# Return the number of valid splits in nums.

class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        n = len(nums)
        prefix = [0] * (n+1)
        ans = 0
        for i in range(n):
            prefix[i+1] = prefix[i] + nums[i]
        for i in range(1, n):
            if prefix[i] >= (prefix[-1] - prefix[i]): ans += 1
        return ans
# time complexity: O(n)
# space cmplexity: O(n)

# https://leetcode.com/problems/left-and-right-sum-differences
# difficulty: easy
# topics: array, prefix sum

# description:
# You are given a 0-indexed integer array nums of size n.
# Define two arrays leftSum and rightSum where:
#   leftSum[i] is the sum of elements to the left of the index i in the array nums. If there is no such element, leftSum[i] = 0.
#   rightSum[i] is the sum of elements to the right of the index i in the array nums. If there is no such element, rightSum[i] = 0.
# Return an integer array answer of size n where answer[i] = |leftSum[i] - rightSum[i]|.

class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        n = len(nums)
        left, right = [0] * n, [0] * n
        for i in range(1, n):
            left[i] = nums[i-1] + left[i-1]
            right[n-i-1] = nums[n-i] + right[n-i]
        return [abs(right[i] - left[i]) for i in range(n)]
# time complexity: O(n)
# space complexity: O(n)

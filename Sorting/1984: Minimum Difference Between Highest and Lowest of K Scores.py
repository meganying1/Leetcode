# https://leetcode.com/problems/minimum-difference-between-highest-and-lowest-of-k-scores/
# difficulty: easy
# topics: array, sliding window, sorting

# description:
# You are given a 0-indexed integer array nums, where nums[i] represents the score of the ith student. You are also given an integer k.
# Pick the scores of any k students from the array so that the difference between the highest and the lowest of the k scores is minimized.
# Return the minimum possible difference.

class Solution:
  def minimumDifference(self, nums: List[int], k: int) -> int:
      if k == 1: return 0
      nums.sort()
      n = len(nums)
      ans = float("inf")
      for i in range(n-k+1):
          ans = min(ans, nums[i+k-1] - nums[i])
      return ans
# time complexity: O(nlogn)
# space complexity: O(n)

# https://leetcode.com/problems/longest-harmonious-subsequence/
# topics: array, hash table, sliding window, sorting, counting
# difficulty: easy

# problem:
# We define a harmonious array as an array where the difference between its maximum value and its minimum value is exactly 1.
# Given an integer array nums, return the length of its longest harmonious subsequence among all its possible subsequences.

class Solution:
    def findLHS(self, nums: List[int]) -> int:
        ans = 0
        counts = Counter(nums)
        for val in counts:
            if val + 1 in counts: ans = max(ans, counts[val] + counts[val+1])
        return ans
# time complexity: O(n)
# space complexity: O(n)

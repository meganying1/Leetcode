# https://leetcode.com/problems/longest-balanced-subarray-i/
# difficulty: medium
# topics: array, hash table, divide and conquer, segment tree, prefix sum

# description:
# You are given an integer array nums.
# A subarray is called balanced if the number of distinct even numbers in the subarray is equal to the number of distinct odd numbers.
# Return the length of the longest balanced subarray.

class Solution:
    def longestBalanced(self, nums: List[int]) -> int:
        n, ans = len(nums), 0
        for i in range(n):
            evenSet, oddSet = set(), set()
            for j in range(i, n):
                if nums[j] % 2 == 0: evenSet.add(nums[j])
                else: oddSet.add(nums[j])
                if len(evenSet) == len(oddSet): ans = max(ans, j-i+1)
        return ans
# time complexity: O(n^3)
  # outer for loop runs n times and inner for loop runs n times
  # each inner iteration takes O(n) time because we find the length of evenSet and oddSet
# space complexity: O(n)

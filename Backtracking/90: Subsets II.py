# https://leetcode.com/problems/subsets-ii
# difficulty: medium
# topics: array, backtracking, bit manipulation

# problem:
# Given an integer array nums that may contain duplicates, return all possible subsets (the power set).
# The solution set must not contain duplicate subsets. Return the solution in any order.

class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        length = len(nums)
        ans = []
        path = []
         
        def backtrack(i):
            if i == length:
                ans.append(path[:])
                return
            path.append(nums[i])
            backtrack(i+1)
            path.pop()
            while i < length-1 and nums[i] == nums[i+1]: i += 1
            backtrack(i+1)

        backtrack(0)
        return ans
  # time complexity: O(n * 2^n)
  # space complexity: O(n)

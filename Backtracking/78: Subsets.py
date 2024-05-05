# https://leetcode.com/problems/subsets/
# difficulty: medium
# topics: array, backtracking, bit manipulation

# problem:
# Given an integer array nums of unique elements, return all possible subsets (the power set).

The solution set must not contain duplicate subsets. Return the solution in any order.

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        length = len(nums)
        visited = [False] * length
        ans = [[]]
         
        def traverse(i, path):
            ans.append(path)
            visited[i] = True
            for j in range(i+1, length):
                if not visited[j]: traverse(j, path + [nums[j]])
            visited[i] = False

        for i in range(length):
            if not visited[i]: traverse(i, [nums[i]])
        
        return ans

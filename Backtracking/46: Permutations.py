# https://leetcode.com/problems/permutations/
# difficulty: medium
# topics: array, backtracking

# problem:
# Given an array nums of distinct integers, return all the possible permutations. You can return the answer in any order.

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        length = len(nums)
        visited = [False] * length
        ans = []
        path = []

        def backtrack(ind, currLen):
            if currLen == length:
                ans.append(path[:])
                return
            visited[ind] = True
            for j in range(length):
                if not visited[j]:
                    path.append(nums[j])
                    backtrack(j, currLen+1)
                    path.pop()
            visited[ind] = False

        for i in range(length):
            path.append(nums[i])
            backtrack(i, 1)
            path.pop()
        return ans

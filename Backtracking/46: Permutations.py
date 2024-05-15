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
# time complexity: O(n * n!)
#     first layer of tree has 1 node, second has 1*2 nodes, third has 1*2*3 nodes, fourth has 1*2*3*4 nodes, etc. -> number of nodes is n!
#     each node takes n time
#         for loop takes n time, but not every iteration of the for loop creates a child
#         as you go deeper down the tree, each node has fewer and fewer children
#         you can mentally model this as all the non-leaf nodes take n time to do a for loop and all the leaf nodes take n time to serialize
# space complexity: O(n)

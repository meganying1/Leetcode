# https://leetcode.com/problems/permutations/
# difficulty: medium
# topics: array, backtracking

# problem:
# Given an array nums of distinct integers, return all the possible permutations. You can return the answer in any order.

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        length = len(nums)
        seen = set()
        ans, path = [], []

        def backtrack():
            if len(path) == length:
                ans.append(path[:])
                return
            for num in nums:
                if num in seen: continue
                path.append(num)
                seen.add(num)
                backtrack()
                seen.remove(num)
                path.pop()

        backtrack()
        return ans
# on a given iteration of the backtrack, we haven’t yet chosen what the next number will be
# index variable is replaced by restructuring the code to not have the backtrack function receive what the next number is immediately 
# we no longer need a outer for loop because we are not locked into any first number, code chooses all possible first numbers
# time complexity: O(n * n!)
#     first layer of tree has 1 node, second has 1*2 nodes, third has 1*2*3 nodes, fourth has 1*2*3*4 nodes, etc. -> number of nodes is n!
#     each node takes n time
#         for loop takes n time, but not every iteration of the for loop creates a child
#         as you go deeper down the tree, each node has fewer and fewer children
#         you can mentally model this as all the non-leaf nodes take n time to do a for loop and all the leaf nodes take n time to serialize
# space complexity: O(n)

"""
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
"""
# when backtrack(index, currLength) is called, whatever is in that index variable is for sure the next node you are visiting, so it is marked as visited immediately
# might be a bit easier if the index represents a decision that is to be made 

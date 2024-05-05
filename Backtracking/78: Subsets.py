# https://leetcode.com/problems/subsets/
# difficulty: medium
# topics: array, backtracking, bit manipulation

# problem:
# Given an integer array nums of unique elements, return all possible subsets (the power set).
# The solution set must not contain duplicate subsets. Return the solution in any order.

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        length = len(nums)
        ans = []
         
        def backtrack(i, path):
            if i == length:
                ans.append(path)
                return
            backtrack(i+1, path)
            backtrack(i+1, path + [nums[i]])

        backtrack(0, [])
        return ans
# time complexity: O(n * 2^n)
    # visualize the code as a tree: each node is a subset
    # there are 2^n subsets for a set of size n of unique elements
    # each node takes n time because we are adding path and [nums[i]] together
# space complexity: O(n^2)
    # when we have a callstack, each execution context for a function is holding some data
        # root call has variable path, which is size 0 at the root
        # but when we call root.left, it has a different path variable with different data
    # at bottom of tree, every call in the callstack is holding data for its own path variable, which can’t be garbage collected yet
        # only when context is popped off callstack can the memory it was holding onto be released and collected
    # each layer of the tree occupies n space, and there are n layers

"""
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        length = len(nums)
        ans = [[]]
         
        def traverse(i, path):
            ans.append(path)
            for j in range(i+1, length): traverse(j, path + [nums[j]])

        for i in range(length): traverse(i, [nums[i]])
        return ans
"""
# be wary of adding arrays together

"""
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
"""
# we don't need to keep track of which elements have been visited
    # visited array exists to prevent entering into a cell that is already in your path 
    # if you’re able to iterate over the input array in order, and decide to include or not include an element, it isn’t needed
# inside a call to traverse(i, nums[i]), we append to our path, mark as visited, and loop over n next elements
    # if an element isn't visited, we try adding to our path and recursing
    # path is up to size n, so path + [nums[j]] takes n time
# for a given recursive call, we have up to n children for the recursion
    # branching factor is at worst n
    # we have tree of depth n and each node recurses to n children, resulting in a tree of size n^n

# https://leetcode.com/problems/maximum-product-of-splitted-binary-tree/
# difficulty: medium
# topics: tree, depth-first search, binary tree

# description: Given an array of positive integers nums, remove the smallest subarray (possibly empty) such that the sum of the remaining elements is divisible by p. It is not allowed to remove the whole array.
# Return the length of the smallest subarray that you need to remove, or -1 if it's impossible.
# A subarray is defined as a contiguous block of elements in the array.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxProduct(self, root: Optional[TreeNode]) -> int:
        ans = total = 0

        def dfs(node):
            nonlocal ans, total
            if not node: return 0
            currSum = node.val + dfs(node.left) + dfs(node.right)
            if node == root: total = currSum
            else: ans = max(ans, currSum * (total-currSum))
            return currSum

        dfs(root)
        dfs(root)
        return ans % (10**9 + 7)
# time complexity: O(n)
# space complexity: O(

# https://leetcode.com/problems/sum-of-root-to-leaf-binary-numbers/
# difficulty: easy
# topics: tree, depth-first search, binary tree

# description:
# You are given the root of a binary tree where each node has a value 0 or 1. Each root-to-leaf path represents a binary number starting with the most significant bit.
#   For example, if the path is 0 -> 1 -> 1 -> 0 -> 1, then this could represent 01101 in binary, which is 13.
# For all leaves in the tree, consider the numbers represented by the path from the root to that leaf. Return the sum of these numbers.
# The test cases are generated so that the answer fits in a 32-bits integer.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        ans = 0
        
        def dfs(node, currSum):
            nonlocal ans
            currSum <<= 1
            currSum += node.val
            if not node.left and not node.right:
                ans += currSum
                return
            if node.left: dfs(node.left, currSum)
            if node.right: dfs(node.right, currSum)
        
        dfs(root, 0)
        return ans
# time complexity: O(n)
# space complexity: O(h), where h is the max depth of the tree

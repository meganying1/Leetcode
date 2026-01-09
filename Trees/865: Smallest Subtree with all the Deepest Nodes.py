# https://leetcode.com/problems/maximum-depth-of-binary-tree/
# difficulty: medium
# topics: hash table, tree, depth-first search, breadth-first search, binary tree

# description:
# Given the root of a binary tree, the depth of each node is the shortest distance to the root.
# Return the smallest subtree such that it contains all the deepest nodes in the original tree.
# A node is called the deepest if it has the largest depth possible among any node in the entire tree.
# The subtree of a node is a tree consisting of that node, plus the set of all descendants of that node.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def subtreeWithAllDeepest(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        def dfs(node):
            if not node: return (0, None)
            leftDepth, leftLca = dfs(node.left)
            rightDepth, rightLca = dfs(node.right)
            if leftDepth == rightDepth: return (leftDepth + 1, node)
            if leftDepth > rightDepth: return (leftDepth + 1, leftLca)
            return (rightDepth + 1, rightLca)
        
        return dfs(root)[1]
# if the left and right subtrees of a node have the same depth, that means they contain the deepest nodes

# time complexity: O(n)
# space complexity: O(n)

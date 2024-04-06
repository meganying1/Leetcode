# https://leetcode.com/problems/validate-binary-search-tree/description/
# difficulty: medium
# topics: tree, depth-first search, breadth-first search, binary tree

# problem:
# Given the root of a binary tree, determine if it is a valid binary search tree (BST).
# A valid BST is defined as follows:
#   The left subtree of a node contains only nodes with keys less than the node's key.
#   The right subtree of a node contains only nodes with keys greater than the node's key.
#   Both the left and right subtrees must also be binary search trees.

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        def helper(node, start, end):
            if not node: return True
            if node.val <= start or node.val >= end: return False
            return helper(node.left, start, node.val) and helper(node.right, node.val, end)

        return helper(root, -float('inf'), float('inf'))
# time complexity: O(n)
# space complexity: O(height of root)

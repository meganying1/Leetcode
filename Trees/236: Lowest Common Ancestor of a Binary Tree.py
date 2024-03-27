# https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/description/
# difficulty: medium
# topics: tree, depth-first search, binary tree

# problem:
# Given a binary tree, find the lowest common ancestor (LCA) of two given nodes in the tree.
# According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes p and q as the lowest node in T that has both p and q as descendants (where we allow a node to be a descendant of itself).”

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root or root.val == p.val or root.val == q.val: return root
        leftSearch = self.lowestCommonAncestor(root.left, p, q)
        rightSearch = self.lowestCommonAncestor(root.right, p, q)
        if not rightSearch: return leftSearch
        if not leftSearch: return rightSearch
        return root

# https://leetcode.com/problems/subtree-of-another-tree/description/
# difficulty: easy
# topics: tree, depth-first search, string matching, binary tree, hash function

# problem:
# Given the roots of two binary trees root and subRoot, return true if there is a subtree of root with the same structure and node values of subRoot and false otherwise.
# A subtree of a binary tree tree is a tree that consists of a node in tree and all of this node's descendants. The tree tree could also be considered as a subtree of itself.

class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        def sameTree(root1, root2):
            if not root1 and not root2: return True
            if not root1 or not root2: return False
            return root1.val == root2.val and sameTree(root1.left, root2.left) and sameTree(root1.right, root2.right)
        
        if not root: return False
        if sameTree(root, subRoot): return True
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)

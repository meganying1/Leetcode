# https://leetcode.com/problems/subtree-of-another-tree/description/
# difficulty: easy
# topics: tree, depth-first search, string matching, binary tree, hash function

# problem:
# Given the roots of two binary trees root and subRoot, return true if there is a subtree of root with the same structure and node values of subRoot and false otherwise.
# A subtree of a binary tree tree is a tree that consists of a node in tree and all of this node's descendants. The tree tree could also be considered as a subtree of itself.

class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root: return False
        if self.sameTree(root, subRoot): return True
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)

    def sameTree(self, root1, root2):
        if not root1 and not root2: return True
        if not root1 or not root2: return False
        return root1.val == root2.val and self.sameTree(root1.left, root2.left) and self.sameTree(root1.right, root2.right)
# n represents # of nodes in root, m represents # of nodes in subroot
# time complexity: O(n * min(n, m))
#     sameTree takes min(n, m) time
#     we make n calls to sameTree
# space complexity: O(height of root)
#     we have callstack of size n, but each call on the callstack does not have a callstack of size min(n, m) because calls to sameTree happen one after another
#     entire sameTree process is self-contained

"""
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        def sameTree(root1, root2):
            if not root1 and not root2: return True
            if not root1 or not root2: return False
            return root1.val == root2.val and sameTree(root1.left, root2.left) and sameTree(root1.right, root2.right)
        
        if not root: return False
        if sameTree(root, subRoot): return True
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
"""
# thhis is inefficient because you have a callstack of calls to isSubtree, but each call to isSubtree creates a new function object of sameTree

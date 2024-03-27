# https://leetcode.com/problems/diameter-of-binary-tree/description/
# difficulty: easy
# topics: tree, depth-first search, binary tree

# problem:
# Given the root of a binary tree, return the length of the diameter of the tree.
# The diameter of a binary tree is the length of the longest path between any two nodes in a tree. This path may or may not pass through the root.
# The length of a path between two nodes is represented by the number of edges between them.

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        ans = 0

        def dfs(root):
            nonlocal ans
            if not root: return 0
            left, right = dfs(root.left), dfs(root.right)
            ans = max(ans, left+right)
            return 1 + max(left, right)
        
        dfs(root)
        return ans
# time complexity: O(n)
# space complexity: O(height)
#     O(log(n)) for balanced tree
#     O(n) for stick tree

# https://leetcode.com/problems/balanced-binary-tree/
# difficulty: easy
# topics: tree, depth-first search, binary tree

# problem:
# Given a binary tree, determine if it is height-balanced.

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        ans = True
        
        def dfs(root):
            nonlocal ans
            if not root or not ans: return 0
            left, right = dfs(root.left), dfs(root.right)
            if abs(left-right) > 1: ans = False
            return 1 + max(left, right)
        
        dfs(root)
        return ans
# time complexity: O(n)
# space complexity: O(height)

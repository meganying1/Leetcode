class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        ans = True
        
        def dfs(root):
            nonlocal ans
            if not root: return 0
            left, right = dfs(root.left), dfs(root.right)
            if abs(left-right) > 1: ans = False
            return 1 + max(left, right)
        
        dfs(root)
        return ans

# https://leetcode.com/problems/binary-tree-inorder-traversal/description/
# difficulty: easy
# topics: stack, tree, depth-first search, binary tree

# problem: 
# Given the root of a binary tree, return the postorder traversal of its nodes' values.

class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root: return []
        return self.postorderTraversal(root.left) + self.postorderTraversal(root.right) + [root.val]

class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ans = []
        if root:
            if root.left: ans.extend(self.postorderTraversal(root.left))
            if root.right: ans.extend(self.postorderTraversal(root.right))
            ans.append(root.val)
        return ans

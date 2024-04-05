# https://leetcode.com/problems/binary-tree-inorder-traversal/description/
# difficulty: easy
# topics: stack, tree, depth-first search, binary tree

# problem:
# Given the root of a binary tree, return the inorder traversal of its nodes' values.

class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root: return []
        return self.inorderTraversal(root.left) + [root.val] + self.inorderTraversal(root.right)

class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ans = []
        if root:
            if root.left: ans.extend(self.inorderTraversal(root.left))
            ans.append(root.val)
            if root.right: ans.extend(self.inorderTraversal(root.right))
        return ans

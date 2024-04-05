# https://leetcode.com/problems/binary-tree-preorder-traversal/description/
# difficulty: easy
# topics: stack, tree, depth-first search, binary tree

# problem:
# Given the root of a binary tree, return the preorder traversal of its nodes' values.

class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root: return []
        return [root.val] + self.preorderTraversal(root.left) + self.preorderTraversal(root.right)

class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ans = []
        if root:
            ans.append(root.val)
            if root.left: ans.extend(self.preorderTraversal(root.left))
            if root.right: ans.extend(self.preorderTraversal(root.right))
        return ans

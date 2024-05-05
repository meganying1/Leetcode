# https://leetcode.com/problems/binary-tree-preorder-traversal/description/
# difficulty: easy
# topics: stack, tree, depth-first search, binary tree

# problem:
# Given the root of a binary tree, return the preorder traversal of its nodes' values.

class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        def preorder(node):
            if not node:
                return
            res.append(node.val)
            preorder(node.left)
            preorder(node.right)
        preorder(root)
        return res
# time complexity: O(n)
# space complexity: O(height of tree)

"""
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root: return []
        return [root.val] + self.preorderTraversal(root.left) + self.preorderTraversal(root.right)
"""
# also be cautious of adding arrays: addition is extension
# same time complexity as previous solution
# usually try to have one array and pass it around rather than continuously making new arrays

"""
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ans = []
        if root:
            ans.append(root.val)
            if root.left: ans.extend(self.preorderTraversal(root.left))
            if root.right: ans.extend(self.preorderTraversal(root.right))
        return ans
"""
# be cautious of using extend
# worst case time complexity: O(n^2)
# best case time complexity: O(nlogn)
    # there are logn levels to the tree and each level takes O(n) time

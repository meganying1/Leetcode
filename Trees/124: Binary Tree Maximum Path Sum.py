# https://leetcode.com/problems/binary-tree-maximum-path-sum/description/
# difficulty: hard
# topics: dynammic programming, tree, depth-first search, binary tree

# problem:
# A path in a binary tree is a sequence of nodes where each pair of adjacent nodes in the sequence has an edge connecting them. A node can only appear in the sequence at most once. Note that the path does not need to pass through the root.
# The path sum of a path is the sum of the node's values in the path.
# Given the root of a binary tree, return the maximum path sum of any non-empty path.

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        ans = -float("inf")
        
        def maxPathSumHelper(root):
            nonlocal ans
            if not root: return 0
            leftMax = max(0, maxPathSumHelper(root.left))
            rightMax = max(0, maxPathSumHelper(root.right))
            currMax = root.val + max(leftMax, rightMax)
            ans = max(ans, currMax, root.val + leftMax + rightMax)
            return currMax
        
        maxPathSumHelper(root)
        return ans

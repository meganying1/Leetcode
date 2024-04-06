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
        
        def maxPathSumHelper(node):
            nonlocal ans
            if not root: return 0
            leftMax = max(0, maxPathSumHelper(node.left))
            rightMax = max(0, maxPathSumHelper(node.right))
            currMax = node.val + max(leftMax, rightMax)
            ans = max(ans, currMax, node.val + leftMax + rightMax)
            return currMax
        
        maxPathSumHelper(root)
        return ans
# time complexity: O(n)
# space complexity: O(height of root)
# important takeaway:
#     when you need to figure out some result for something, you can try to figure out the result for every X
#     and if you try it for all X, you have the result

"""
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
"""
# doing two things: constructing currMax and updating the answer
# could getCurrMax function: dedicated to getting the currMax for a given node, where currMax is “the max sum starting from this node, descending down a chain children"
#     answer to overall problem then can be separated into two steps:
#         inner function is just a dfs function that goes through all nodes and applies getCurrMax function
#     if we can get getCurrMax to run in O(1) time on average, overall function runs in O(n) time
#         if we spend n time preprocessing / filling out the cache table, then all future calls will take O(1)
#         as long as we make at least n future calls, we can say each call to the function, overall, takes constant time on average

# doesn't matter the order of we check the nodes in: could be preorder, inorder, or postorder

# don't shadow variables (named parameter in helper root, which shares a name with the outer function)
#     can be unclear which root is being referred to

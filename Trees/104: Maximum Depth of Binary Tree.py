# https://leetcode.com/problems/maximum-depth-of-binary-tree/description/
# difficulty: easy
# topics: tree, breadth-first search, depth-first search, binary tree

# problem:
# Given the root of a binary tree, return its maximum depth.
# A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root: return 0
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))
# a tree has two stages:
#     the first stage is where you recurse down i.e. send out the fishing line
#     the second stage is where you bubble information back up i.e. reel the line back in
# this manifests in two discrete parts of the code:
#     you need to determine the recursive aspect going down
#     and the relevant information to bubble back up

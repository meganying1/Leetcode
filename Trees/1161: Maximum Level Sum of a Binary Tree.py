# https://leetcode.com/problems/maximum-level-sum-of-a-binary-tree/
# difficulty: medium
# topics: tree, depth-first search, breadth-first search, binary tree

# description:
# Given the root of a binary tree, the level of its root is 1, the level of its children is 2, and so on.
# Return the smallest level x such that the sum of all the values of nodes at level x is maximal.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        maxTotal, level = -float("inf"), 1
        queue = deque([root])
        while queue:
            total = 0
            for i in range(len(queue)):
                node = queue.popleft()
                total += node.val
                if node.left: queue.append(node.left)
                if node.right: queue.append(node.right)
            if total > maxTotal:
                maxTotal, ans = total, level
            level += 1
        return ans
# time complexity: O(n)
# space complexity: O(n)
#   best case scenario: O(1)
#     if we have a linear tree with 1 node at each level
#     only 1 node will be stored in the queue at a time
#   worst case scenario: O(n)
#     if we have a complete tree with a height of h, the last level will have 2^h nodes and the max length of queue is 2^h
#     since 1 + 2 + 4 + ... + 2^h = n, 2^h = (n+1) / 2
#     therefore, space complexity is O(2^h) 

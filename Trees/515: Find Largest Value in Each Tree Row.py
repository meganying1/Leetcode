# https://leetcode.com/problems/find-largest-value-in-each-tree-row/
# difficulty: medium
# topics: tree, depth-first search, breadth-first search, binary tree

# problem:
# Given the root of a binary tree, return an array of the largest value in each row of the tree (0-indexed).

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        if not root: return []
        ans = []
        queue = deque()
        queue.append(root)
        while queue:
            n = len(queue)
            currMax = -float("inf")
            for _ in range(n):
                curr = queue.popleft()
                currMax = max(currMax, curr.val)
                if curr.left: queue.append(curr.left)
                if curr.right: queue.append(curr.right)
            ans.append(currMax)
        return ans
  # time complexity: O(n)
  # space complexity: O(n)

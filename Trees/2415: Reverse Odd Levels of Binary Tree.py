# https://leetcode.com/problems/reverse-odd-levels-of-binary-tree/description/
# difficulty: medium
# topics: tree, breadth-first search, depth-first search, binary tree

# problem:
# Given the root of a perfect binary tree, reverse the node values at each odd level of the tree.
# For example, suppose the node values at level 3 are [2,1,3,4,7,11,29,18], then it should become [18,29,11,7,4,3,1,2].
# Return the root of the reversed tree.
# A binary tree is perfect if all parent nodes have two children and all leaves are on the same level.
# The level of a node is the number of edges along the path between it and the root node.

from collections import deque

class Solution:
    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        queue = deque()
        queue.append(root)
        level = 0
        
        def reverseLevel():
            left, right = 0, len(queue)-1
            while left < right:
                queue[left].val, queue[right].val = queue[right].val, queue[left].val
                left += 1
                right -= 1

        while queue:
            if level % 2 == 1:
                reverseLevel()
            n = len(queue)
            for _ in range(n):
                curr = queue.popleft()
                if curr.left: queue.append(curr.left)
                if curr.right: queue.append(curr.right)
            level += 1

        return root
# time complexity: O(n)
# space complexity: O(n)

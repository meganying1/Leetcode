# https://leetcode.com/problems/minimum-number-of-operations-to-sort-a-binary-tree-by-level/
# difficulty: medium
# topics: tree, breadth-first search, binary tree

# problem:
# You are given the root of a binary tree with unique values.
# In one operation, you can choose any two nodes at the same level and swap their values.
# Return the minimum number of operations needed to make the values at each level sorted in a strictly increasing order.
# The level of a node is the number of edges along the path between it and the root node.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minimumOperations(self, root: Optional[TreeNode]) -> int:
        queue = deque()
        ans = 0
        queue.append(root)
        while queue:
            n = len(queue)
            layer = []
            indexMap = {}
            for i in range(n):
                curr = queue.popleft()
                layer.append(curr.val)
                indexMap[curr.val] = i
                if curr.left: queue.append(curr.left)
                if curr.right: queue.append(curr.right)
            sortedLayer = sorted(layer)
            for i in range(n):
                if layer[i] != sortedLayer[i]:
                    ans += 1
                    neededIndex = indexMap[sortedLayer[i]]
                    layer[i], layer[neededIndex] = layer[neededIndex], layer[i]
                    indexMap[layer[neededIndex]] = neededIndex
        return ans
# time complexity: O(nlogn)
# space complexity: O(n)

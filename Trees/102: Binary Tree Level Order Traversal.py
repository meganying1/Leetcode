# https://leetcode.com/problems/binary-tree-level-order-traversal/
# difficulty: medium
# topics: tree, breadth-first search, binary tree

# problem:
# Given the root of a binary tree, return the level order traversal of its nodes' values. (i.e., from left to right, level by level).

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root: return []
        queue = deque()
        queue.append(root)
        ans = []
        while len(queue) > 0:
            level = []
            for i in range(len(queue)):
                curr = queue.popleft()
                level.append(curr.val)
                if curr.left: queue.append(curr.left)
                if curr.right: queue.append(curr.right)
            ans.append(level)
        return ans

"""
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        nodeDict = defaultdict(list)

        def search(root, level):
            nonlocal nodeDict
            if not root: return
            nodeDict[level].append(root.val)
            search(root.left, level+1)
            search(root.right, level+1)

        search(root, 0)
        return [val for val in nodeDict.values()]
"""

# https://leetcode.com/problems/binary-tree-level-order-traversal/
# difficulty: medium
# topics: tree, breadth-first search, binary tree

# problem:
# Given the root of a binary tree, return the level order traversal of its nodes' values. (i.e., from left to right, level by level).

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        queue = deque()
        queue.append(root)
        ans = []
        while queue:
            level = []
            for i in range(len(queue)):
                curr = queue.popleft()
                level.append(curr.val)
                if curr.left: queue.append(curr.left)
                if curr.right: queue.append(curr.right)
            ans.append(level)
        return ans
# time complexity: O(n)
# space complexity: O(n)
#     dependent on max number of nodes in a level, which is equal to n/2

"""
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
# can use 'while queue' or 'while len(queue)' instead of 'while len(queue) > 0'
# don't need initial case: 'if not root: return []'

"""
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        levelToVals = defaultdict(list)

        def search(root, level):
            nonlocal levelToVals
            if not root: return
            levelToVals[level].append(root.val)
            search(root.left, level+1)
            search(root.right, level+1)

        search(root, 0)
        return [val for val in levelToVals.values()]
"""
# time complexity: O(n)
# space complexity: O(height of tree)

# don't need nonlocal here
#     nonlocal exists, because in python, reassigning a variable is indistinguishable from initializing a variable, due to the syntax of the language
#     nonlocal tells the code if we are initializing a new variable inside the function, or if we are reassigning an existing variable outside our scope
# equals sign means we are trying to reassign or initialize, and we need to distinguish
#     writing nonlocal nodeDict here is bad because we aren't using “=“ or trying to reassign nodeDict, we're just changing the keys/values inside it
#     you should usually not reassign hashmaps; the point of a hashmap is to mutate it, add keys/values, etc

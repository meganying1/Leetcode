# https://leetcode.com/problems/binary-tree-right-side-view/description/
# difficulty: medium
# topics: tree, depth-first search, breadth-first search, binary tree

# problem: 
# Given the root of a binary tree, imagine yourself standing on the right side of it, return the values of the nodes you can see ordered from top to bottom.

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        ans, queue = [], deque()
        if root: queue.append(root)
        while queue:
            for i in range(len(queue)):
                node = queue.popleft()
                if node.left: queue.append(node.left)
                if node.right: queue.append(node.right)
            ans.append(node.val)
        return ans
# time complexity: O(n)
# space complexity: O(n)

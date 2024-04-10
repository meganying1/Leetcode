# https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/description/
# difficulty: medium
# topics: array, hash table, divide and conquer, tree, binary tree

# problem:
# Given two integer arrays preorder and inorder where preorder is the preorder traversal of a binary tree and inorder is the inorder traversal of the same tree, construct and return the binary tree.

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        n = len(inorder)
        inorderPos = {}
        for i in range(n): inorderPos[inorder[i]] = i
        
        def helper(preStart, preEnd, inStart, inEnd):

            # if preStart > preEnd, size of subtree is 0
            if preStart > preEnd: return None

            # root is first val in preorder array
            val = preorder[preStart]
            newNode = TreeNode(val)
            inInd = inorderPos[val]

            # size of left subtree is equal to inorder index of root minus start of inorder array
            leftSize = inorderPos[val] - inStart

            # size of right subtree is equal to end of inorder array minus inorder index of root
            rightSize = inEnd - inorderPos[val]

            # index of preorder start of left subtree is next value in preorder
            # index of preorder end of left subtree is current start value plus left size
            newNode.left = helper(preStart+1, preStart+leftSize, inStart, inInd-1)

            # index of preorder start of right subtree is next value in preorder after all left subtree nodes
            # index of preorder end of right subtree is current end value
            newNode.right = helper(preStart+leftSize+1, preEnd, inInd+1, inEnd)
            return newNode

        return helper(0, n-1, 0, n-1)
# time complexity: O(n)
# space complexity: O(n)

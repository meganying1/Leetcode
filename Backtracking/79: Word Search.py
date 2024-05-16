# https://leetcode.com/problems/word-search/
# difficulty: medium
# topics: array, string, backtracking, matrix

# problem:
# Given an m x n grid of characters board and a string word, return true if word exists in the grid.
# The word can be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring. The same letter cell may not be used more than once.

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows, cols = len(board), len(board[0])
        length = len(word)
        visited = set()

        def isValid(row, col):
            return row >= 0 and row < rows and col >= 0 and col < cols
        
        def backtrack(row, col, i):
            if board[row][col] != word[i]: return False
            if i == length-1: return True
            visited.add((row, col))
            for direction in [(0, -1), (0, 1), (-1, 0), (1, 0)]:
                newRow, newCol = row + direction[0], col + direction[1]
                if (isValid(newRow, newCol) and (newRow, newCol) not in visited and 
                backtrack(newRow, newCol, i+1)): return True
            visited.remove((row, col))
            return False

        for row in range(rows):
            for col in range(cols):
                if backtrack(row, col, 0): return True
        return False
# time complexity: O(m * n * 3^k)
# space complexity: O(k)

"""
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows, cols = len(board), len(board[0])
        length = len(word)
        visited = [[False] * cols for i in range(rows)]

        def isValid(row, col):
            return row >= 0 and row < rows and col >= 0 and col < cols
        
        def backtrack(row, col, i):
            if board[row][col] != word[i]: return False
            if i == length-1: return True
            visited[row][col] = True
            for direction in [(0, -1), (0, 1), (-1, 0), (1, 0)]:
                newRow, newCol = row + direction[0], col + direction[1]
                if (isValid(newRow, newCol) and not visited[newRow][newCol] and 
                backtrack(newRow, newCol, i+1)): return True
            visited[row][col] = False
            return False
            
        for row in range(rows):
            for col in range(cols):
                if backtrack(row, col, 0): return True
        return False
"""
# time complexity: O(m * n * 3^k)
#     branching factor is at most 3 for all decisions except first one
#     depth of recursion is k (length of word)
#     we create m * n trees
# space complexity: O(m * n)
#     can optimize space by using a set

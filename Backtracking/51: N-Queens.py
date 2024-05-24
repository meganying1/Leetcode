# https://leetcode.com/problems/n-queens/description/
# difficulty: hard
# topics: array, backtracking

# problem:
# The n-queens puzzle is the problem of placing n queens on an n x n chessboard such that no two queens attack each other.
# Given an integer n, return all distinct solutions to the n-queens puzzle. You may return the answer in any order.
# Each solution contains a distinct board configuration of the n-queens' placement, where 'Q' and '.' both indicate a queen and an empty space, respectively.

class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        queenCols, ans = [], []
        cols, diags1, diags2 = set(), set(), set()

        def backtrack(row):
            if row == n:
                ans.append(["".join(["." * col, "Q", "." * (n-col-1)]) for col in queenCols])
                return
            for col in range(n):
                if col in cols or n-row+col in diags1 or n+row+col in diags2: continue
                cols.add(col)
                diags1.add(n-row+col)
                diags2.add(n+row+col)
                queenCols.append(col)
                backtrack(row+1)
                cols.remove(col)
                diags1.remove(n-row+col)
                diags2.remove(n+row+col)
                queenCols.pop()

        backtrack(0)
        return ans
# time complexity: O(n^2 * n!)
# space complexity: O(n)

"""
class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        board, ans = [], []
        cols, diags1, diags2 = set(), set(), set()

        def backtrack(row):
            if row == n:
                ans.append(board[:])
                return
            for col in range(n):
                if col in cols or n-row+col in diags1 or n+row+col in diags2: continue
                cols.add(col)
                diags1.add(n-row+col)
                diags2.add(n+row+col)
                board.append("".join(["." * col, "Q", "." * (n-col-1)]))
                backtrack(row+1)
                cols.remove(col)
                diags1.remove(n-row+col)
                diags2.remove(n+row+col)
                board.pop()

        backtrack(0)
        return ans
"""
# time complexity: O(n^2 * n!)
#     the tree has n! nodes
#         first layer has n nodes, second layer has n-1 nodes, etc.
#     non-leaf nodes take O(n^2) time
#         for loop takes O(n) time, and append inside of for loop takes O(n) time
#     leaf nodes also take O(n^2) time
#         each solution has n strings of length n, so it takes n^2 time to copy over the solution
# space complexity: O(n^2)
#     callstack has depth of n, and the seen sets take O(n) space
#     board takes n^2 space

"""
class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        colIndices, ans = [], []
        cols, diags1, diags2 = set(), set(), set()

        def createBoard():
            board = []
            for idx in colIndices:
                row = []
                for i in range(idx): row.append(".")
                row.append("Q")
                for i in range(n-idx-1): row.append(".")
                board.append("".join(row))
            return board

        def backtrack(row):
            if row == n:
                ans.append(createBoard())
                return
            for col in range(n):
                if col in cols or n-row+col in diags1 or n+row+col in diags2: continue
                cols.add(col)
                diags1.add(n-row+col)
                diags2.add(n+row+col)
                colIndices.append(col)
                backtrack(row+1)
                cols.remove(col)
                diags1.remove(n-row+col)
                diags2.remove(n+row+col)
                colIndices.pop()

        backtrack(0)
        return ans
"""

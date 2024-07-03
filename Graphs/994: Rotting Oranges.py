# https://leetcode.com/problems/rotting-oranges/
# difficulty: medium
# topics: array, breadth-first search, matrix

# problem:
# You are given an m x n grid where each cell can have one of three values:
#   0 representing an empty cell,
#   1 representing a fresh orange, or
#   2 representing a rotten orange.
# Every minute, any fresh orange that is 4-directionally adjacent to a rotten orange becomes rotten.
# Return the minimum number of minutes that must elapse until no cell has a fresh orange. If this is impossible, return -1.

class Solution(object):
    def orangesRotting(self, grid):
        rows, cols = len(grid), len(grid[0])
        visited = set()
        ans = fresh = 0
        queue = deque()
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2: queue.append((r, c, 0))
                elif grid[r][c] == 1: fresh += 1

        def isValid(r, c):
            return r >= 0 and r < rows and c >= 0 and c < cols
        
        while queue:
            (r, c, t) = queue.popleft()
            ans = max(ans, t)
            for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                newR, newC = r+dx, c+dy
                if not isValid(newR, newC) or grid[newR][newC] != 1 or (newR, newC) in visited: continue
                fresh -= 1
                visited.add((newR, newC))
                queue.append((newR, newC, t+1))
        return ans if fresh == 0 else -1
# time complexity: O(n*m)
# space complexity: O(n*m)

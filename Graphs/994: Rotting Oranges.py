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

class Solution:
    def orangesRotting(self, grid):
        rows, cols = len(grid), len(grid[0])
        visited = set()
        ans = fresh = 0
        queue = deque()
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2: queue.append((r, c))
                elif grid[r][c] == 1: fresh += 1

        def isValid(r, c):
            return r >= 0 and r < rows and c >= 0 and c < cols

        while queue:
            ans += 1
            for _ in range(len(queue)):
                r, c = queue.popleft()
                for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                    newR, newC = r+dx, c+dy
                    if not isValid(newR, newC) or grid[newR][newC] != 1 or (newR, newC) in visited: continue
                    fresh -= 1
                    if fresh == 0: return ans
                    visited.add((newR, newC))
                    queue.append((newR, newC))
        return -1
# time complexity: O(n*m)
# space complexity: O(n*m)
# this is called multisource bfs because we start a bfs at multiple starting points at the same time
# can reduce the space by reusing input matrix as our seen set, would drop memory complexity to min(n, m) just for the deque

"""
class Solution(object):
    def orangesRotting(self, grid):
        rows, cols = len(grid), len(grid[0])
        visited = set()
        t = fresh = 0
        queue = deque()
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2: queue.append((r, c, t))
                elif grid[r][c] == 1: fresh += 1

        def isValid(r, c):
            return r >= 0 and r < rows and c >= 0 and c < cols

        while queue:
            (r, c, t) = queue.popleft()
            for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                newR, newC = r+dx, c+dy
                if not isValid(newR, newC) or grid[newR][newC] != 1 or (newR, newC) in visited: continue
                fresh -= 1
                visited.add((newR, newC))
                queue.append((newR, newC, t+1))
        return t if fresh == 0 else -1
"""
# don't want to keep track of t in queue, because whole point of queue / bfs is that it goes in order
# can avoid this by getting a count of how big the next layer is, and then popping all of the nodes in the layer in one group

# https://leetcode.com/problems/pacific-atlantic-water-flow/
# difficulty: medium
# topics: array, breadth-first search, depth-first search, matrix

# problem:
# There is an m x n rectangular island that borders both the Pacific Ocean and Atlantic Ocean. The Pacific Ocean touches the island's left and top edges, and the Atlantic Ocean touches the island's right and bottom edges.
# The island is partitioned into a grid of square cells. You are given an m x n integer matrix heights where heights[r][c] represents the height above sea level of the cell at coordinate (r, c).
# The island receives a lot of rain, and the rain water can flow to neighboring cells directly north, south, east, and west if the neighboring cell's height is less than or equal to the current cell's height. Water can flow from any cell adjacent to an ocean into the ocean.
# Return a 2D list of grid coordinates result where result[i] = [ri, ci] denotes that rain water can flow from cell (ri, ci) to both the Pacific and Atlantic oceans.

class Solution(object):
    def pacificAtlantic(self, heights):
        rows, cols = len(heights), len(heights[0])
        seen = set()
        pacificFlow = [[False for c in range(cols)] for r in range(rows)]
        atlanticFlow = [[False for c in range(cols)] for r in range(rows)]
        pacificQueue = deque()
        atlanticQueue = deque()

        def isValid(r, c, newR, newC):
            return (newR >= 0 and newR < rows and newC >= 0 and newC < cols and
            heights[newR][newC] >= heights[r][c])
        
        def bfs(queue, canFlow):
            ans = set()
            while queue:
                r, c = queue.popleft()
                ans.add((r, c))
                for dr, dc in [(0, -1), (0, 1), (-1, 0), (1, 0)]:
                    newR, newC = r+dr, c+dc
                    if not isValid(r, c, newR, newC): continue
                    if canFlow[newR][newC]: continue
                    canFlow[newR][newC] = True
                    queue.append((newR, newC))
            return ans

        for r in range(rows):
            for c in range(cols):
                if r == 0 or c == 0:
                    pacificFlow[r][c] = True
                    pacificQueue.append((r, c))
                if r == rows-1 or c == cols-1:
                    atlanticFlow[r][c] = True
                    atlanticQueue.append((r, c))

        pacific = bfs(pacificQueue, pacificFlow)
        atlantic = bfs(atlanticQueue, atlanticFlow)
        return pacific.intersection(atlantic)
# time complexity: O(n*m)
#     bfs can only visit each element and edge once
#     we call bfs twice
# space complexity: O(n*m)

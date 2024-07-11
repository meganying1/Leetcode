# https://leetcode.com/problems/making-a-large-island/
# difficutly: hard
# topics: array, depth-first search, breadth-first search, union find, matrix

# problem:
# You are given an n x n binary matrix grid. You are allowed to change at most one 0 to be 1.
# Return the size of the largest island in grid after applying this operation.
# An island is a 4-directionally connected group of 1s.

class Solution(object):
    def largestIsland(self, grid):
        rows, cols = len(grid), len(grid[0])
        seenCell = set()
        islandMap, sizeMap = {}, {}
        ans, island = 1, 0

        def isValid(i, j):
            return (i >= 0) and (i < rows) and (j >= 0) and (j < cols)
    
        def getNeighbor(i, j):
            ans = 0
            seenIsland = set()
            for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                newI, newJ = i+dx, j+dy
                if isValid(newI, newJ) and ((newI, newJ) in sizeMap) and (islandMap[(newI, newJ)] not in seenIsland):
                    seenIsland.add(islandMap[(newI, newJ)])
                    ans += sizeMap[(newI, newJ)]
            return ans
        
        def getIslandSize(i, j, maxNeighbor):
            if not isValid(i, j) or ((i, j) in seenCell): return (0, maxNeighbor)
            if grid[i][j] == 0:
                maxNeighbor = max(maxNeighbor, getNeighbor(i, j)+1)
                return (0, maxNeighbor)
            ans = 1
            seenCell.add((i, j))
            currCells.add((i, j))
            for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                (size, maxNeighbor) = getIslandSize(i+dx, j+dy, maxNeighbor)
                ans += size
            return (ans, maxNeighbor)

        for r in range(rows):
            for c in range(cols):
                if (r, c) not in seenCell and grid[r][c] == 1:
                    currCells = set()
                    maxNeighbor = 0
                    (size, maxNeighbor) = getIslandSize(r, c, maxNeighbor)
                    for key in currCells:
                        sizeMap[key] = size
                        islandMap[key] = island
                    ans = max(ans, size + maxNeighbor)
                    island += 1
        return ans

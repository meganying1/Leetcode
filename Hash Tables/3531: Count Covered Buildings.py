# https://leetcode.com/problems/count-covered-buildings/
# difficulty: medium
# topics: array, hash table, sorting

# description:
# You are given a positive integer n, representing an n x n city. You are also given a 2D grid buildings, where buildings[i] = [x, y] denotes a unique building located at coordinates [x, y].
# A building is covered if there is at least one building in all four directions: left, right, above, and below.
# Return the number of covered buildings.

class Solution:
    def countCoveredBuildings(self, n: int, buildings: List[List[int]]) -> int:
        ans = 0
        xToY, yToX = defaultdict(list), defaultdict(list)
        for x, y in buildings:
            xToY[x].append(y)
            yToX[y].append(x)
        for y in xToY.values():
            y.sort()
        for x in yToX.values():
            x.sort()
        for x, y in buildings:
            if xToY[x][0] < y and xToY[x][-1] > y and yToX[y][0] < x and yToX[y][-1] > x: ans += 1 
        return ans
# time complexity: O(mlogm), where m is len(buildings)
#   building maps takes O(m) time
#   sorting values in each map takes O(mlogm) time in the worst case scenario
# space complexity: O(m)
#   we store all m coordinates

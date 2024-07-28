# https://leetcode.com/problems/find-the-city-with-the-smallest-number-of-neighbors-at-a-threshold-distance/?envType=daily-question&envId=2024-07-28
# difficulty: medium
# topics: dynamic programming, graph, shortest path

# problem:
# There are n cities numbered from 0 to n-1. Given the array edges where edges[i] = [fromi, toi, weighti] represents a bidirectional and weighted edge between cities fromi and toi, and given the integer distanceThreshold.
# Return the city with the smallest number of cities that are reachable through some path and whose distance is at most distanceThreshold, If there are multiple such cities, return the city with the greatest number.
# Notice that the distance of a path connecting cities i and j is equal to the sum of the edges' weights along that path.

class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        distDict = [[float("inf")] * n for _ in range(n)]
        for i in range(n): distDict[i][i] = 0
        for origin, dest, weight in edges:
            distDict[origin][dest] = weight
            distDict[dest][origin] = weight
        for k in range(n):
            for i in range(n):
                for j in range(n):
                    distDict[i][j] = min(distDict[i][j], distDict[i][k]+distDict[k][j])
        countDict = defaultdict(list)
        for i in range(n):
            count = 0
            for j in range(n):
                if i == j: continue
                if distDict[i][j] <= distanceThreshold: count += 1
            countDict[count].append(i)
        ans = countDict[min(countDict.keys())]
        return ans[0] if len(ans) == 1 else max(ans)

# time complexity: O(n^3)
# space complexity: O(n^2)
# uses the floyd-warshall algorithm to find shortest path between all nodes in weighted graph, which can handle negatively and positively weights
#   shortest path between i to j will have some k number of intermediate nodes
#   idea behind algorithm is to treat each and every vertex from 1 to n as an intermediate node one by one
#   for every pair (i, j) of the source and destination vertices respectively, there are two possible cases:
#       k is not an intermediate vertex in shortest path from i to j, so we keep the value of dist[i][j] as it is
#       k is an intermediate vertex in shortest path from i to j, so we update the value of dist[i][j] as dist[i][k] + dist[k][j] if dist[i][j] > dist[i][k] + dist[k][j]

# https://leetcode.com/problems/minimum-cost-to-convert-string-i/
# difficulty: medium
# topics: array, string, graph theory, shortest path

# description:
# You are given two 0-indexed strings source and target, both of length n and consisting of lowercase English letters. You are also given two 0-indexed character arrays original and changed, and an integer array cost, where cost[i] represents the cost of changing the character original[i] to the character changed[i].
# You start with the string source. In one operation, you can pick a character x from the string and change it to the character y at a cost of z if there exists any index j such that cost[j] == z, original[j] == x, and changed[j] == y.
# Return the minimum cost to convert the string source to the string target using any number of operations. If it is impossible to convert source to target, return -1.
# Note that there may exist indices i, j such that original[j] == original[i] and changed[j] == changed[i].

class Solution:
    def minimumCost(self, source: str, target: str, original: List[str], changed: List[str], cost: List[int]) -> int:
        n, m = len(source), len(original)
        ans = 0
        dist = [[float('inf')] * 26 for _ in range(26)]
        for i in range(m):
            row, col = ord(original[i]) - ord('a'), ord(changed[i]) - ord('a')
            dist[row][col] = min(dist[row][col], cost[i])
        for i in range(26):
            dist[i][i] = 0
        for k in range(26):
            for i in range(26):
                for j in range(26):
                    if dist[i][k] != float('inf') and dist[k][j] != float('inf'):
                        dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
        for i in range(n):
            ans += dist[ord(source[i]) - ord('a')][ord(target[i]) - ord('a')]
        return ans if ans != float("inf") else -1
# time complexity: O(n + m + 26^3)
# space complexity: O(26^3)

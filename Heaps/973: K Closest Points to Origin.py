# https://leetcode.com/problems/k-closest-points-to-origin/
# difficulty: medium
# topics: array, math, divide and conquer, geometry, sorting, heap (priority queue), quickselect

# problem:
# Given an array of points where points[i] = [xi, yi] represents a point on the X-Y plane and an integer k, return the k closest points to the origin (0, 0).
# The distance between two points on the X-Y plane is the Euclidean distance (i.e., √(x1 - x2)2 + (y1 - y2)2).
# You may return the answer in any order. The answer is guaranteed to be unique (except for the order that it is in).

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        def distance(x, y):
            return x**2 + y**2

        heap = []
        for [x, y] in points[:k]: heapq.heappush(heap, (-distance(x, y), x, y))
        for [x, y] in points[k:]:
            (d, minx, miny) = heap[0]
            if distance(x, y) > d:
                heapq.heappushpop(heap, (-distance(x, y), x, y))
        return [[x, y] for (d, x, y) in heap]
# time complexity: O(n * logk)
# space complexity: O(n)

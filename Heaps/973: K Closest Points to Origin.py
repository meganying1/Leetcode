# https://leetcode.com/problems/k-closest-points-to-origin/
# difficulty: medium
# topics: array, math, divide and conquer, geometry, sorting, heap (priority queue), quickselect

# problem:
# Given an array of points where points[i] = [xi, yi] represents a point on the X-Y plane and an integer k, return the k closest points to the origin (0, 0).
# The distance between two points on the X-Y plane is the Euclidean distance (i.e., √(x1 - x2)2 + (y1 - y2)2).
# You may return the answer in any order. The answer is guaranteed to be unique (except for the order that it is in).

# heap solution
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

# quickselect solution
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        def distance(x, y):
            return x**2 + y**2
        
        def quickselect(arr, k):
            n = len(arr)
            randInd = random.randint(0, n-1)
            randDist = arr[randInd][2]
            left, middle, right = [], [], []
            for p in arr:
                if p[2] > randDist: right.append(p)
                elif p[2] < randDist: left.append(p)
                else: middle.append(p)
            leftLen, midLen = len(left), len(middle)
            if leftLen == k: return left
            elif leftLen > k: return quickselect(left, k)
            elif leftLen < k and k <= leftLen + midLen:
                left.extend(middle[:k-leftLen])
                return left
            left.extend(middle)
            left.extend(quickselect(right, k-leftLen-midLen))
            return left
        
        for p in points:
            p.append(distance(p[0], p[1]))
        return [[p[0], p[1]] for p in quickselect(points, k)]

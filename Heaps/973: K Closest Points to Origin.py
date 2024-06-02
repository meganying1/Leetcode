class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        def distance(x, y):
            return x**2 + y**2

        heap = []
        heapq.heapify(heap)
        for [x, y] in points[:k]: heapq.heappush(heap, (-distance(x, y), x, y))
        for [x, y] in points[k:]:
            (d, minx, miny) = heap[0]
            if distance(x, y) > d:
                heapq.heappushpop(heap, (-distance(x, y), x, y))
        return [[x, y] for (d, x, y) in heap]

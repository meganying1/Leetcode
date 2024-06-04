# https://leetcode.com/problems/find-median-from-data-stream/
# difficulty: hard
# topics: two pointers, design, sorting, heap (priority queue), data stream)

# problem:
# The median is the middle value in an ordered integer list. If the size of the list is even, there is no middle value, and the median is the mean of the two middle values.
#   For example, for arr = [2,3,4], the median is 3.
#   For example, for arr = [2,3], the median is (2 + 3) / 2 = 2.5.
# Implement the MedianFinder class:
#   MedianFinder() initializes the MedianFinder object.
#   void addNum(int num) adds the integer num from the data stream to the data structure.
#   double findMedian() returns the median of all elements so far. Answers within 10-5 of the actual answer will be accepted.

class MedianFinder:

    def __init__(self):
        self.minHeap = []
        self.maxHeap = []

    def addNum(self, num: int) -> None:
        if len(self.minHeap) == len(self.maxHeap):
            heapq.heappush(self.minHeap, -heapq.heappushpop(self.maxHeap, -num))
        else:
            heapq.heappush(self.maxHeap, -heapq.heappushpop(self.minHeap, num))

    def findMedian(self) -> float:
        if len(self.minHeap) == len(self.maxHeap): return (self.minHeap[0]-self.maxHeap[0])/2
        return self.minHeap[0]
# time complexity: O(nlogn)
#     we add n numbers, and it takes log(n/2) time to add
#     log(n/2) = logn - log2 -> simplifies to logn time
# space complexity: O(n)

# https://leetcode.com/problems/kth-largest-element-in-a-stream/
# difficulty: easy
# topics: tree, design, binary search tree, heap (priority queue), binary tree, data stream

# problem:
# Design a class to find the kth largest element in a stream. Note that it is the kth largest element in the sorted order, not the kth distinct element.
# Implement KthLargest class:
#   KthLargest(int k, int[] nums) Initializes the object with the integer k and the stream of integers nums.
#   int add(int val) Appends the integer val to the stream and returns the element representing the kth largest element in the stream.

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.len = 0
        self.heap = []
        heapq.heapify(self.heap)
        for n in nums: self.add(n)

    def add(self, val: int) -> int:
        if self.len < self.k:
            heapq.heappush(self.heap, val)
            self.len += 1
        elif self.heap[0] < val: heapq.heappushpop(self.heap, val)
        return self.heap[0]

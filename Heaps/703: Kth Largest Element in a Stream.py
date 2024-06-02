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
# time complexity: O(n + k * logk)
#     builtin heapify takes O(n) time
#     popping takes O(logk) time and we pop k times
# space complexity: O(k)

"""
class minHeap:

    def __init__(self, nums, k):
        self.nums = []
        self.len = 0
        self.k = k
        for val in nums: self.heappush(val)
    
    def siftup(self, i):
        while i//2 >= 0:
            if self.nums[i//2] > self.nums[i]:
                self.nums[i//2], self.nums[i] = self.nums[i], self.nums[i//2]
                i //= 2
            else: return
        
    def minchild(self, i):
        if 2*i + 1 >= self.len or self.nums[2*i] < self.nums[2*i + 1]: return 2*i
        return 2*i + 1
    
    def siftdown(self, i):
        while 2*i < self.len:
            minI = self.minchild(i)
            if self.nums[i] > self.nums[self.minchild(i)]:
                self.nums[minI], self.nums[i] = self.nums[i], self.nums[minI]
                i = minI
            else: return

    def heappush(self, val):
        if self.len < self.k:
            self.nums.append(val)
            self.len += 1
            self.siftup(self.len-1)
        elif val > self.nums[0]:
            self.nums[0] = val
            self.siftdown(0)

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.heap = minHeap(nums, k)

    def add(self, val: int) -> int:
        self.heap.heappush(val)
        return self.heap.nums[0]
"""
# for practice implementing heap class
# time complexity: O(nlogn)
#     heapify takes O(nlogn) time
#     popping takes O(klogn) time

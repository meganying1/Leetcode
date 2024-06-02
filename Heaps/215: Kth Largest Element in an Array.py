# https://leetcode.com/problems/kth-largest-element-in-an-array/
# difficulty: medium
# topics: array, divide and conquer, sorting, heap (priority queue), quickselect)

# problem:
# Given an integer array nums and an integer k, return the kth largest element in the array.
# Note that it is the kth largest element in the sorted order, not the kth distinct element.
# Can you solve it without sorting?

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = nums[:k]
        heapq.heapify(heap)
        for val in nums[k:]:
            if val > heap[0]: heapq.heappushpop(heap, val)
        return heap[0]
# time complexity: O(n + klogk)

"""
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heapq.heapify(nums)
        for _ in range(len(nums)-k): heapq.heappop(nums)
        return nums[0]
"""

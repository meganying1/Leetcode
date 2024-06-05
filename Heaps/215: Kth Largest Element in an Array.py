# https://leetcode.com/problems/kth-largest-element-in-an-array/
# difficulty: medium
# topics: array, divide and conquer, sorting, heap (priority queue), quickselect)

# problem:
# Given an integer array nums and an integer k, return the kth largest element in the array.
# Note that it is the kth largest element in the sorted order, not the kth distinct element.
# Can you solve it without sorting?

# heap solution
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = nums[:k]
        heapq.heapify(heap)
        for val in nums[k:]:
            if val > heap[0]: heapq.heappushpop(heap, val)
        return heap[0]
# time complexity: O((n-k) * logk)
#     we push onto the heap n-k times in the worst case scenario and heappushpop takes O(logk) time where k is the size of the heap
# space complexity: O(n)
#     we have a heap of size k
#     we create an array of size n-k in the for loop

"""
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heapq.heapify(nums)
        for _ in range(len(nums)-k): heapq.heappop(nums)
        return nums[0]
"""

# quickselect solution
"""
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        n = len(nums)
        
        def partition(l, r):
            x = nums[r]
            i = l
            for j in range(l, r):
                if nums[j] <= x:
                    nums[i], nums[j] = nums[j], nums[i]
                    i += 1
            nums[i], nums[r] = nums[r], nums[i]
            return i
        
        def helper(l, r):
            i = partition(l, r)
            if n-i == k: return nums[i]
            elif n-i > k: return helper(l+1, r)
            return helper(l, r-1)

        return helper(0, n-1)
"""
# worst case scenario time complexity is O(n^2)
#     to fix: choose random index instead of r as pivot

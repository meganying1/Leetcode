# https://leetcode.com/problems/find-subsequence-of-length-k-with-the-largest-sum/
# topics: array, hash table, sorting, priority queue (heap)
# difficulty: easy

# problem: 
# You are given an integer array nums and an integer k. You want to find a subsequence of nums of length k that has the largest sum.
# Return any such subsequence as an integer array of length k.
# A subsequence is an array that can be derived from another array by deleting some or no elements without changing the order of the remaining elements.

class Solution:
    def maxSubsequence(self, nums: List[int], k: int) -> List[int]:
        sortSubsequence = sorted([(v, i) for i, v in enumerate(nums)])[-k:]
        sortSubsequence.sort(key=lambda x:x[1])
        return [v for (v, i) in sortSubsequence]
# time complexity: O(nlogn + klogk)
#   we iterate through all n elements to create an array of tuples containing the values and indices, and sorting our array takes O(nlogn) time
#   creating a slice of the largest k elements takes O(k) time, and sorting our new array takes O(klogk) time
#   we then iterate through all k elements in our sorted array to return our answer
# space complexity: O(sort + n + k)

"""
class Solution:
    def maxSubsequence(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        maxHeap = [(-nums[i], i) for i in range(n)]
        heapq.heapify(maxHeap)
        ans = []
        for _ in range(k):
            n, i = heapq.heappop(maxHeap)
            ans.append((-n, i))
        ans.sort(key=lambda x:x[1])
        return [n for (n, i) in ans]
"""
# time complexity: O(klogn + klogk)
#   building maxHeap takes O(n) time
#   popping from a heap takes O(logn) time, and we pop from maxHeap k times for a total of O(klogn) time
#   sorting our ans array takes O(klogk) time
# space complexity: O(sort + n + k)

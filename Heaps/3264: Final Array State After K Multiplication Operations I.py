# https://leetcode.com/problems/final-array-state-after-k-multiplication-operations-i/
# difficulty: easy
# topics: array, math, heap (priority queue), simulation

# You are given an integer array nums, an integer k, and an integer multiplier.
# You need to perform k operations on nums. In each operation:
#   Find the minimum value x in nums. If there are multiple occurrences of the minimum value, select the one that appears first.
#   Replace the selected minimum value x with x * multiplier.
# Return an integer array denoting the final state of nums after performing all k operations.

class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        minHeap = [(x, i) for i, x in enumerate(nums)]
        heapq.heapify(minHeap)
        for _ in range(k):
            _, i = heapq.heappop(minHeap)
            nums[i] *= multiplier
            heapq.heappush(minHeap, (nums[i], i))
        return nums
# time complexity: O(n + klogn)
#   creating minHeap and running heapify take O(n) time
#   for loop runs k times
#   in for loop, heappop and heappush take O(logn) time
# space complexity: O(n)

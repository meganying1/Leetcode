# https://leetcode.com/problems/maximal-score-after-applying-k-operations/
# difficulty: medium
# topics: array, greedy, heap (priority queue)

# problem:
# You are given a 0-indexed integer array nums and an integer k. You have a starting score of 0.
# In one operation:
#   choose an index i such that 0 <= i < nums.length,
#   increase your score by nums[i], and
#   replace nums[i] with ceil(nums[i] / 3).
# Return the maximum possible score you can attain after applying exactly k operations.
# The ceiling function ceil(val) is the least integer greater than or equal to val.

class Solution:
    def maxKelements(self, nums: List[int], k: int) -> int:
        numsHeap = []
        for num in nums:
            heapq.heappush(numsHeap, -num)
        ans = 0
        for _ in range(k):
            currMax = -heapq.heappop(numsHeap)
            ans += currMax
            heapq.heappush(numsHeap, -ceil(currMax / 3))
        return ans
# time complexity: O(nlogn)
#   O(nlogn) time to add all n nums to heap
#   O(klogn) time to pop from heap k times
#   n > k
# space complexity: O(n)

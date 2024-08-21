# https://leetcode.com/problems/find-k-th-smallest-pair-distance
# difficulty: hard
# topics: array, two pointers, binary search, sorting

# problem:
# The distance of a pair of integers a and b is defined as the absolute difference between a and b.
# Given an integer array nums and an integer k, return the kth smallest distance among all the pairs nums[i] and nums[j] where 0 <= i < j < nums.length.

class Solution:
    def smallestDistancePair(self, nums: List[int], k: int) -> int:
        n = len(nums)
        nums.sort()
        lo, hi = 0, nums[-1]-nums[0]

        def getNumPairs(dist):
            start = end = ans = 0
            while end < n:
                while nums[end]-nums[start] > dist: start += 1
                ans += end-start
                end += 1
            return ans

        while lo < hi:
            mid = (lo+hi) // 2
            numPairs = getNumPairs(mid)
            if numPairs >= k: hi = mid
            else: lo = mid+1
        return lo
# we use binary search to find kth smallest distance, and then use sliding window to count number of pairs with distances less than or equal to current midpoint distance
# time complexity: O(n*logm + sort), where n is length of nums and m is maximum possible distance
      # binary search takes O(logm) time and sliding window technique to get number of pairs takes O(n) time
# space complexity: O(sort)

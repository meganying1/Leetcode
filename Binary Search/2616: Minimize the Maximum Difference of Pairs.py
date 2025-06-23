# https://leetcode.com/problems/minimize-the-maximum-difference-of-pairs
# topics: array, binary search, dynamic programming, greedy, sorting
# difficulty: medium

# problem:
# You are given a 0-indexed integer array nums and an integer p. Find p pairs of indices of nums such that the maximum difference amongst all the pairs is minimized. Also, ensure no index appears more than once amongst the p pairs.
# Note that for a pair of elements at the index i and j, the difference of this pair is |nums[i] - nums[j]|, where |x| represents the absolute value of x.
# Return the minimum maximum difference among all p pairs. We define the maximum of an empty set to be zero.

class Solution:
    def minimizeMax(self, nums: List[int], p: int) -> int:
        nums.sort()
        n = len(nums)
        lo, hi = 0, nums[-1]-nums[0]

        def canFindPairs(mid):
            i = pairs = 0
            while i < n-1:
                if nums[i+1] - nums[i] <= mid:
                    pairs += 1
                    i += 1
                i += 1
            return pairs >= p

        while lo < hi:
            mid = lo + ((hi - lo) // 2)
            if canFindPairs(mid): hi = mid
            else: lo = mid+1
        return lo
# time complexity: O(nlogn + nlogv), where n is len(nums) and v is max(nums)-min(nums)
#   sorting takes O(nlogn) time
#   binary search takes a total of O(nlogv) time
#     the right boundary of the search space is v, so binary search takes logv steps
#     canFindPairs takes O(n) time
# space complexity: O(sort)

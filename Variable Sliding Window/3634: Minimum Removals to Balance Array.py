# https://leetcode.com/problems/minimum-removals-to-balance-array/
# difficulty: medium
# topics: array, sliding window, sorting

# description:
# You are given an integer array nums and an integer k.
# An array is considered balanced if the value of its maximum element is at most k times the minimum element.
# You may remove any number of elements from nums​​​​​​​ without making it empty.
# Return the minimum number of elements to remove so that the remaining array is balanced.
# Note: An array of size 1 is considered balanced as its maximum and minimum are equal, and the condition always holds true.

class Solution:
    def minRemoval(self, nums: List[int], k: int) -> int:
        nums.sort()
        n = len(nums)
        l = ans = 0
        for r in range(n):
            while nums[l] * k < nums[r]: l += 1
            ans = max(ans, r-l+1)
        return n-ans
# time complexity: O(nlogn)
# space complexity: O(n)

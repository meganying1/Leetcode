# https://leetcode.com/problems/minimize-maximum-pair-sum-in-array/
# difficulty: medium
# topics: array, two pointers, greedy, sorting

# description:
# The pair sum of a pair (a,b) is equal to a + b. The maximum pair sum is the largest pair sum in a list of pairs.
# For example, if we have pairs (1,5), (2,3), and (4,4), the maximum pair sum would be max(1+5, 2+3, 4+4) = max(6, 5, 8) = 8.
# Given an array nums of even length n, pair up the elements of nums into n / 2 pairs such that:
#   Each element of nums is in exactly one pair, and
#   The maximum pair sum is minimized.
# Return the minimized maximum pair sum after optimally pairing up the elements.

class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)
        ans = 0
        for i in range(n // 2):
            ans = max(ans, nums[i] + nums[n-i-1])
        return ans
# time complexity: O(nlogn)
# space complexity: O(n)

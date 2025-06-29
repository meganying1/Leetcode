# https://leetcode.com/problems/maximum-value-of-an-ordered-triplet-ii/
# topics: array
# difficulty: medium

# problem:
# You are given a 0-indexed integer array nums.
# Return the maximum value over all triplets of indices (i, j, k) such that i < j < k. If all such triplets have a negative value, return 0.
# The value of a triplet of indices (i, j, k) is equal to (nums[i] - nums[j]) * nums[k].

class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        n = len(nums)
        ans = 0
        prefixMax, suffixMax = [num for num in nums], [num for num in nums]
        for i in range(1, n):
            prefixMax[i] = max(nums[i-1], prefixMax[i-1])
        for i in range(n-2, -1, -1):
            suffixMax[i] = max(nums[i+1], suffixMax[i+1])
        for i in range(1, n-1):
            ans = max(ans, (prefixMax[i]-nums[i]) * suffixMax[i])
        return ans
# time cmplexity: O(n)
# space complexity: O(n)
      
# consider each element of the list excluding the first or last item, calculate what the maximum value of a triplet of indices would be if that element was the center index
#     (maximum value) = ((prefix maximum) - (the element)) * (postfix maximum)

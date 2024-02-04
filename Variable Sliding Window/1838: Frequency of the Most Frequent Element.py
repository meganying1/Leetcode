# https://leetcode.com/problems/longest-substring-with-at-least-k-repeating-characters/description/
# difficulty: medium
# hash table, string, divide and conquer, sliding window

# problem:
# Given a string s and an integer k, return the length of the longest substring of s such that the frequency of each character in this substring is greater than or equal to k.
# If no such substring exists, return 0.

class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        length = len(nums)
        nums.sort()
        start, end = length-1, length-1
        currSum = nums[end]
        ans = 1
        while start >= 0:
            while start > 0 and (nums[end] * (end-start+1)) - currSum <= k:
                ans = max(ans, end-start+1)
                start -= 1
                currSum += nums[start]
            if (nums[end] * (end-start+1)) - currSum <= k: ans = max(ans, end-start+1)
            while (nums[end] * (end-start+1)) - currSum > k:
                currSum -= nums[end]
                end -= 1
            start -= 1
            currSum += nums[start]
        return ans

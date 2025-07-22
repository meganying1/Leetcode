# https://leetcode.com/problems/maximum-erasure-value/
# topics: array, hash table, sliding window
# difficulty: medium

# problem:
# You are given an array of positive integers nums and want to erase a subarray containing unique elements. The score you get by erasing the subarray is equal to the sum of its elements.
# Return the maximum score you can get by erasing exactly one subarray.
# An array b is called to be a subarray of a if it forms a contiguous subsequence of a, that is, if it is equal to a[l],a[l+1],...,a[r] for some (l,r).

class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        seen = set()
        l = r = currSum = 0
        n = len(nums)
        ans = -float('inf')
        while r < n:
            while nums[r] in seen:
                seen.remove(nums[l])
                currSum -= nums[l]
                l += 1
            seen.add(nums[r])
            currSum += nums[r]
            r += 1
            ans = max(currSum, ans)
        return ans
# time complexity: O(n)
# space complexity: O(n)

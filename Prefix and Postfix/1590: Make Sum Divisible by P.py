# https://leetcode.com/problems/make-sum-divisible-by-p/
# difficulty: medium
# topics: array, hash table, prefix sum

# description: 
# Given an array of positive integers nums, remove the smallest subarray (possibly empty) such that the sum of the remaining elements is divisible by p. It is not allowed to remove the whole array.

# Return the length of the smallest subarray that you need to remove, or -1 if it's impossible.

# A subarray is defined as a contiguous block of elements in the array.

class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        neededSum = sum(nums) % p
        if neededSum == 0: return 0
        ans, n = float("inf"), len(nums)
        prefixSum = 0
        remainderMap = {}
        for i in range(n):
            prefixSum += nums[i]
            neededRemainder = (prefixSum - neededSum) % p
            if neededRemainder in remainderMap: ans = min(ans, i - remainderMap[neededRemainder])
            remainder = prefixSum % p
            remainderMap[remainder] = i
            if remainder % p == neededSum: ans = min(ans, i+1)
        return ans if ans != float("inf") and ans != n else -1
# method:
#   use prefix sums to calculate subarray sums
#   to make the remaining sum divisible by p, we need (totalSum - subarraySum) % p == 0
#   therefore, we must remove the small subarray where (subarraySum % p) == neededSum, where neededSum = (totalSum % p)
#   a subarray (j+1..i) has subarraySum = (pref[i] - pref[j]), so we want ((pref[i] - pref[j]) % p) == neededSum
#   this means pref[j] == (pref[i] - neededSum) % p
#   at every index i, we check if (pref[i] - neededSum) % p has previously occurred
#   the minimum value of (i - j) is the answer

# time complexity: O(n)
# space complexity: O(n)
#   in the worst case scenario, all n nums have a different remainder

# sliding window method --> TLE
"""
class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        neededSum = sum(nums) % p
        if neededSum == 0: return 0
        ans, n = float("inf"), len(nums)
        for l in range(n):
            currSum, r = 0, l
            while r < n:
                currSum += nums[r]
                if currSum % p == neededSum:
                    ans = min(r-l+1, ans)
                r += 1
        return ans if ans != float("inf") and ans != n else -1
"""
# time complexity: O(n^2)
# space complexity: O(1)

# https://leetcode.com/problems/maximum-sum-of-3-non-overlapping-subarrays/
# difficulty: hard
# topics: array, dynamic programming

# problem:
# Given an integer array nums and an integer k, find three non-overlapping subarrays of length k with maximum sum and return them.
# Return the result as a list of indices representing the starting position of each interval (0-indexed). If there are multiple answers, return the lexicographically smallest one.

# returns indices in array (time limit exceeded)
class Solution:
    def maxSumOfThreeSubarrays(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        currSum = sum(nums[:k])
        sumList = [currSum]
        cache = {}
        for i in range(n-k):
            currSum += nums[i+k] - nums[i]
            sumList.append(currSum)
        
        def dp(i, currSum, remainingArr, indices):
            if remainingArr == 0: return (currSum, indices)
            if i+k > n: return (0, indices)
            key = (i, currSum, remainingArr)
            if key in cache: return (cache[key], indices)
            addArr = dp(i+k, currSum + sumList[i], remainingArr-1, indices + [i])
            skipArr = dp(i+1, currSum, remainingArr, indices)
            ans = max(addArr[0], skipArr[0])
            cache[key] = ans
            if addArr[0] >= skipArr[0]: return addArr
            return skipArr

        result = dp(0, 0, 3, [])[1]
        return result

# returns maximum sum
class Solution:
    def maxSumOfThreeSubarrays(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        currSum = sum(nums[:k])
        sumList = [currSum]
        cache = {}
        for i in range(n-k):
            currSum += nums[i+k] - nums[i]
            sumList.append(currSum)
        
        def dp(i, currSum, remainingArr):
            if remainingArr == 0: return currSum
            if i+k >= n: return 0
            key = (i, currSum, remainingArr)
            if key in cache: return cache[key]
            addArr = dp(i+k, currSum + sumList[i], remainingArr-1)
            skipArr = dp(i+1, currSum, remainingArr)
            ans = max(addArr, skipArr)
            cache[key] = ans
            return ans

        return dp(0, 0, 3)

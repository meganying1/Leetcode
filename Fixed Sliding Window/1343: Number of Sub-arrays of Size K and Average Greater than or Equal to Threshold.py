# https://leetcode.com/problems/number-of-sub-arrays-of-size-k-and-average-greater-than-or-equal-to-threshold/description/
# difficulty: medium
# topics: array, sliding window

# problem:
# Given an array of integers arr and two integers k and threshold, return the number of sub-arrays of size k and average greater than or equal to threshold.

class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        minSum = k * threshold
        length = len(arr)
        start, end = 0, k-1
        currSum = sum(arr[i] for i in range(k))
        ans = 0
        while end < length:
            if currSum >= minSum: ans += 1
            if end+1 == length: break
            currSum -= arr[start]
            currSum += arr[end+1]
            start += 1
            end += 1
        return ans
        
"""
class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        minSum = k * threshold
        length = len(arr)
        start, end = 0, k-1
        currSum = sum(arr[start:end+1])
        ans = 1 if currSum >= minSum else 0
        while end < length-1:
            currSum -= arr[start]
            currSum += arr[end+1]
            start += 1
            end += 1
            if currSum >= minSum: ans += 1
        return ans
"""     
# when writing currSum = sum(arr[start:end+1]), an array of size end-start is created in memory temporarily, increasing space complexity

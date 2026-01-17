# https://leetcode.com/problems/longest-mountain-in-array/
# difficulty: medium
# topics: array, dynamic programming, two pointers

# description:
# You may recall that an array arr is a mountain array if and only if:
#    arr.length >= 3
#   There exists some index i (0-indexed) with 0 < i < arr.length - 1 such that:
#     arr[0] < arr[1] < ... < arr[i - 1] < arr[i]
#     arr[i] > arr[i + 1] > ... > arr[arr.length - 1]
# Given an integer array arr, return the length of the longest subarray, which is a mountain. Return 0 if there is no mountain subarray.

class Solution:
    def longestMountain(self, arr: List[int]) -> int:
        ans = 0
        n = len(arr)
        for i in range(1, n-1):
            l, r = i-1, i+1
            if arr[l] < arr[i] and arr[r] < arr[i]:
                while l >= 0 and arr[l] < arr[l+1]:
                    l -= 1
                while r < n and arr[r] < arr[r-1]:
                    r += 1
                ans = max(ans, r-l-1)
        return ans
# time complexity: O(n)
#   we only visit each element in the array once because once a peak is processed, neighboring indices cannot form another peak that would cause the same expansion again
#   each array index is part of at most one uphill traversal and one downhill traversal
# space complexity: O(1)

# https://leetcode.com/problems/longest-turbulent-subarray/
# difficulty: medium
# topics: array, dynamic programming, sliding window

# problem:
# Given an integer array arr, return the length of a maximum size turbulent subarray of arr.
# A subarray is turbulent if the comparison sign flips between each adjacent pair of elements in the subarray.
# More formally, a subarray [arr[i], arr[i + 1], ..., arr[j]] of arr is said to be turbulent if and only if:
#   For i <= k < j:
#     arr[k] > arr[k + 1] when k is odd, and
#     arr[k] < arr[k + 1] when k is even.
#   Or, for i <= k < j:
#     arr[k] > arr[k + 1] when k is even, and
#     arr[k] < arr[k + 1] when k is odd.

class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        length = len(arr)
        if length == 1: return 1
        ans = 1
        start = end = 0
        turbulenceSize = 0
        oddGreater = False if arr[0] > arr[1] else True
        while end < length-1:
            if (((end % 2 == 0 and arr[end] > arr[end+1]) or 
            (end % 2 == 1 and arr[end] < arr[end+1])) and not oddGreater or
            ((end % 2 == 0 and arr[end] < arr[end+1]) or 
            (end % 2 == 1 and arr[end] > arr[end+1])) and oddGreater):
                turbulenceSize += 1
                ans = max(ans, turbulenceSize+1)
            else:
                turbulenceSize = 0 if arr[end] == arr[end+1] else 1
                start = end+1
                oddGreater = not oddGreater
            end += 1
        return ans

"""
class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        length = len(arr)
        if length == 1: return 1
        ans = 1
        start = end = 0
        turbulenceSize = 0
        while end < length-1:
            if (end % 2 == 0 and arr[end] > arr[end+1]) or (end % 2 == 1 and arr[end] < arr[end+1]):
                turbulenceSize += 1
                ans = max(ans, turbulenceSize+1)
            else:
                start = end+1
                turbulenceSize = 0
            end += 1
        start = end = 0
        turbulenceSize = 0
        while end < length-1:
            if (end % 2 == 0 and arr[end] < arr[end+1]) or (end % 2 == 1 and arr[end] > arr[end+1]):
                turbulenceSize += 1
                ans = max(ans, turbulenceSize+1)
            else:
                start = end+1
                turbulenceSize = 0
            end += 1
        return ans
  """

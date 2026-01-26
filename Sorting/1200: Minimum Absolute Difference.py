# https://leetcode.com/problems/minimum-absolute-difference/
# difficulty: easy
# topics: array, sorting

# description:
# Given an array of distinct integers arr, find all pairs of elements with the minimum absolute difference of any two elements.
# Return a list of pairs in ascending order(with respect to pairs), each pair [a, b] follows
  # a, b are from arr
  # a < b
  # b - a equals to the minimum absolute difference of any two elements in arr

class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort()
        minDiff = float('inf')
        for i in range(1, len(arr)):
            currDiff = arr[i]-arr[i-1]
            if currDiff < minDiff: minDiff, ans = currDiff, [[arr[i-1], arr[i]]]
            elif currDiff == minDiff: ans.append([arr[i-1], arr[i]])
        return ans
# time complexity: O(nlogn)
# space complexity: O(1)

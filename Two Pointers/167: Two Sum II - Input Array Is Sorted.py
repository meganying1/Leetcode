# https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/description/
# difficulty: medium
# topics: array, two pointers, binary search

# problem:
# Given a 1-indexed array of integers numbers that is already sorted in non-decreasing order, find two numbers such that they add up to a specific target number. Let these two numbers be numbers[index1] and numbers[index2] where 1 <= index1 < index2 <= numbers.length.
# Return the indices of the two numbers, index1 and index2, added by one as an integer array [index1, index2] of length 2.
# The tests are generated such that there is exactly one solution. You may not use the same element twice.
# Your solution must use only constant extra space.

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i, j = 0, len(numbers)-1
        while True:
            currSum = numbers[i] + numbers[j]
            if currSum == target: return [i+1, j+1]
            elif currSum < target: i += 1
            else: j -= 1

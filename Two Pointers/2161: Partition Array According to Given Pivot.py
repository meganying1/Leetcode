# https://leetcode.com/problems/partition-array-according-to-given-pivot/
# topics: array, two pointers, simulation
# difficulty: medium

# problem:
# You are given a 0-indexed integer array nums and an integer pivot. Rearrange nums such that the following conditions are satisfied:
#   Every element less than pivot appears before every element greater than pivot.
#   Every element equal to pivot appears in between the elements less than and greater than pivot.
#   The relative order of the elements less than pivot and the elements greater than pivot is maintained.
#     More formally, consider every pi, pj where pi is the new position of the ith element and pj is the new position of the jth element. If i < j and both elements are smaller (or larger) than pivot, then pi < pj.
# Return nums after the rearrangement.

# two pointers solution
class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        n = len(nums)
        ans = [0] * n
        less, greater = 0, n-1
        for i in range(n):
            if nums[i] < pivot:
                ans[less] = nums[i]
                less += 1
            if nums[n-i-1] > pivot:
                ans[greater] = nums[n-i-1]
                greater -= 1
        while less <= greater:
            ans[less] = pivot
            less += 1
        return ans
# time complexity: O(n)
# space complexity: O(n)

class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        less, equal, greater = [], [], []
        for n in nums:
            if n < pivot: less.append(n)
            elif n > pivot: greater.append(n)
            else: equal.append(n)
        return less + equal + greater
# time complexity: O(n)
# space complexity: O(n)

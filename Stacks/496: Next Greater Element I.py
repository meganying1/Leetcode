# https://leetcode.com/problems/next-greater-element-i/
# difficulty: easy
# topics: array, hash table, stack, monotonic stack

# problem:
# The next greater element of some element x in an array is the first greater element that is to the right of x in the same array.
# You are given two distinct 0-indexed integer arrays nums1 and nums2, where nums1 is a subset of nums2.
# For each 0 <= i < nums1.length, find the index j such that nums1[i] == nums2[j] and determine the next greater element of nums2[j] in nums2. If there is no next greater element, then the answer for this query is -1.
# Return an array ans of length nums1.length such that ans[i] is the next greater element as described above.

class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack, ans = [], []
        greaterElemDict = {}
        for i in range(len(nums2)):
            while stack and stack[-1] < nums2[i]:
                last = stack.pop()
                greaterElemDict[last] = nums2[i]
            stack.append(nums2[i])
        for num in nums1:
            if num in greaterElemDict: ans.append(greaterElemDict[num])
            else: ans.append(-1)
        return ans
# time complexity: O(n + m) -> O(m)
#   n is length of nums1 and m is length of nums2
#   m is always greater than n
# space complexity: O(n + m) -> O(m)

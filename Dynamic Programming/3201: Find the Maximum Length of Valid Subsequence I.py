# https://leetcode.com/problems/find-the-maximum-length-of-valid-subsequence-i
# topics: array, dynamic programming
# difficulty: medium

# problem:
# You are given an integer array nums.
# A subsequence sub of nums with length x is called valid if it satisfies:
#   (sub[0] + sub[1]) % 2 == (sub[1] + sub[2]) % 2 == ... == (sub[x - 2] + sub[x - 1]) % 2.
# Return the length of the longest valid subsequence of nums.
# A subsequence is an array that can be derived from another array by deleting some or no elements without changing the order of the remaining elements.

class Solution:
    def maximumLength(self, nums: List[int]) -> int:
        n = len(nums)
        allOdd = allEven = evenOdd = oddEven = 0
        for num in nums:
            if num % 2 == 1:
                allOdd += 1
                if evenOdd % 2 == 1: evenOdd += 1
                if oddEven % 2 == 0: oddEven += 1
            else:
                allEven += 1
                if oddEven % 2 == 1: oddEven += 1
                if evenOdd % 2 == 0: evenOdd += 1
        return max(allOdd, allEven, evenOdd, oddEven)
# time complexity: O(n)
# space complexity: O(1)

# any valid subsequence contains either all even elements, all odd elements, alternate even odd, or alternate odd even
# we can try all 4 possibilities and see which one leads to the maximum length

# https://leetcode.com/problems/maximum-subarray-with-equal-products/
# difficulty: easy

# problem:
# You are given an array of positive integers nums.
# An array arr is called product equivalent if prod(arr) == lcm(arr) * gcd(arr), where:
#   prod(arr) is the product of all elements of arr.
#   gcd(arr) is the GCD of all elements of arr.
#   lcm(arr) is the LCM of all elements of arr.
# Return the length of the longest product equivalent subarray of nums.
# A subarray is a contiguous non-empty sequence of elements within an array.
# The term gcd(a, b) denotes the greatest common divisor of a and b.
# The term lcm(a, b) denotes the least common multiple of a and b.

class Solution:
    def maxLength(self, nums: List[int]) -> int:
        ans = 1
        n = len(nums)
        for start in range(n):
            currProd = currGcd = currLcm = nums[start]
            for end in range(start+1, n):
                currProd *= nums[end]
                currGcd = math.gcd(currGcd, nums[end])
                currLcm = math.lcm(currLcm, nums[end])
                if currProd == currGcd * currLcm: ans = max(ans, end-start+1)
        return ans
# time complexity: O(n^2)
# space complexity: O(1)

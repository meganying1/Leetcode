# https://leetcode.com/problems/four-divisors/
# difficulty: medium
# topics: array, math

# description:
# Given an integer array nums, return the sum of divisors of the integers in that array that have exactly four divisors. If there is no such integer in the array, return 0.

class Solution:
    def sumFourDivisors(self, nums: List[int]) -> int:
        ans = 0
        for n in nums:
            count = total = 0
            for i in range(1, int(n ** 0.5) + 1):
                if n % i == 0:
                    count += 1
                    total += i
                    j = n // i
                    if j != i:
                        count += 1
                        total += j
                    if count > 4: break
            if count == 4: ans += total
        return ans
# time complexity: O(n * sqrt(m)), where n is len(nums) and m is max(m)
# space complexity: O(1)

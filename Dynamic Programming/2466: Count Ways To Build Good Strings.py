# https://leetcode.com/problems/count-ways-to-build-good-strings/
# difficulty: medium
# topics: dynamic programming

# Given the integers zero, one, low, and high, we can construct a string by starting with an empty string, and then at each step perform either of the following:
#   Append the character '0' zero times.
#   Append the character '1' one times.
# This can be performed any number of times.
# A good string is a string constructed by the above process having a length between low and high (inclusive).
# Return the number of different good strings that can be constructed satisfying these properties. Since the answer can be large, return it modulo 10^9 + 7.

class Solution:
    def countGoodStrings(self, low: int, high: int, zero: int, one: int) -> int:
        dp = [0] * (high + 1)
        dp[0] = 1
        for i in range(high+1):
            dp[i] += (dp[i-zero] + dp[i-one]) % (10**9 + 7)
        return sum(dp[low:high+1]) % (10**9 + 7)
# bottom-up dynammic programming
# time complexity: O(high)
# space complexity: O(high)

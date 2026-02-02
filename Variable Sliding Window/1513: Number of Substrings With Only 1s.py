# https://leetcode.com/problems/number-of-substrings-with-only-1s/
# difficulty: medium
# topics: math, string

# description:
# Given a binary string s, return the number of substrings with all characters 1's. Since the answer may be too large, return it modulo 109 + 7.

class Solution:
    def numSub(self, s: str) -> int:
        l = r = ans = 0
        n = len(s)
        mod = (10 ** 9) + 7
        while r < n:
            while l < n and s[l] == '0': l += 1
            r = l
            while r < n and s[r] == '1': r += 1
            length = r-l
            ans += ((length + 1) * length // 2) % mod
            l = r
        return ans % mod
# time complexity: O(n)
# space complexity: O(1)

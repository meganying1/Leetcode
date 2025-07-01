# https://leetcode.com/problems/number-of-substrings-containing-all-three-characters/
# topics: hash table, string, sliding window
# difficulty: medium

# problem:
# Given a string s consisting only of characters a, b and c.
# Return the number of substrings containing at least one occurrence of all these characters a, b and c.

class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        n = len(s)
        counts = {c:0 for c in 'abc'}
        ans = matches = l = r = 0
        while r < n:
            counts[s[r]] += 1
            if counts[s[r]] == 1: matches += 1
            while matches == 3:
                ans += n - r
                counts[s[l]] -= 1
                if counts[s[l]] == 0: matches -= 1
                l += 1
            r += 1
        return ans
# time complexity: O(n)
# space complexity: O(1)

# once we find a substring that is valid, we know that any larger substring that includes that substring is also valid
#     we increment our total count by the number of ways we can extend the substring to the right, which is equal to the length of the string minus the right index of the valid substring
#     we then move the left pointer forward until the substring is no longer valid; while it is valid, we continue adding the number of possible substrings

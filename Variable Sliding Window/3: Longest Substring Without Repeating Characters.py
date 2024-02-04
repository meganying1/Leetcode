# https://leetcode.com/problems/longest-substring-without-repeating-characters/
# difficulty: medium
# topics: hash table, string, sliding window

# problem:
# Given a string s, find the length of the longest substring without repeating characters.

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ans = 0
        start, end = 0, 0
        seen = set()
        while end < len(s):
            while s[end] in seen:
                seen.remove(s[start])
                start += 1
            seen.add(s[end])
            ans = max(ans, end-start+1)
            end += 1
        return ans
# idea:
#     you expand the window by 1 index to the right, and potentially make it invalid
#     you contract the window from the left until it is valid again

"""
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        length = len(s)
        if length == 0: return 0
        ans = 1
        start, end = 0, 0
        seen = set(s[start])
        while end < length-1:
            end += 1
            if s[end] not in seen:
                seen.add(s[end])
                ans = max(ans, end-start+1)
            else:
                while s[end] != s[start]:
                    seen.remove(s[start])
                    start += 1
                start += 1
        return ans
"""
# can be simplified

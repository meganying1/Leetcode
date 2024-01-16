# https://leetcode.com/problems/valid-palindrome-ii/description/
# difficulty: easy
# topics: two pointers, string, greedy

# problem:
# Given a string s, return true if the s can be palindrome after deleting at most one character from it.

class Solution:
    def validPalindrome(self, s: str) -> bool:
        start, end = 0, len(s)-1
        deleted = False
        while start < end:
            if s[start] == s[end]:
                start += 1
                end -= 1
            else:
                str1, str2 = s[start:end], s[start+1:end+1]
                return str1 == str1[::-1] or str2 == str2[::-1]
        return True

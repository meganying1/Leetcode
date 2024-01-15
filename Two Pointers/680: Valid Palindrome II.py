# https://leetcode.com/problems/valid-palindrome-ii/description/
# difficulty: easy
# topics: two pointers, string, greedy

# problem:
# Given a string s, return true if the s can be palindrome after deleting at most one character from it.

class Solution:
    def isPalindrome(self, s):
        return s == s[::-1]

    def validPalindrome(self, s: str) -> bool:
        start, end = 0, len(s)-1
        deleted = False
        while start < end:
            if s[start] == s[end]:
                start += 1
                end -= 1
            else:
                return self.isPalindrome(s[start:end]) or self.isPalindrome(s[start+1:end+1])
        return True

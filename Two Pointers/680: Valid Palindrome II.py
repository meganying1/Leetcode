# https://leetcode.com/problems/valid-palindrome-ii/description/
# difficulty: easy
# topics: two pointers, string, greedy

# problem:
# Given a string s, return true if the s can be palindrome after deleting at most one character from it.

class Solution:
    def validPalindrome(self, s: str) -> bool:
        start, end = 0, len(s)-1

        def isPalindrome(start, end):
            while start < end:
                if s[start] != s[end]: return False
                start += 1
                end -= 1
            return True

        while start < end:
            if s[start] == s[end]:
                start += 1
                end -= 1
                continue
            return isPalindrome(start+1, end) or isPalindrome(start, end-1)
        return True

"""
class Solution:
    def validPalindrome(self, s: str) -> bool:
        start, end = 0, len(s)-1

        def isPalindrome(s, start, end):
            while start < end:
                if s[start] != s[end]: return False
                start += 1
                end -= 1
            return True

        while start < end:
            if s[start] == s[end]:
                start += 1
                end -= 1
                continue
            return isPalindrome(s, start+1, end) or isPalindrome(s, start, end-1)
        return True
"""
# still linear memory usage because it recreates a local variable s in memory

"""
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
"""
# check for palindrome using two pointers to ensure entire solution is O(1) space

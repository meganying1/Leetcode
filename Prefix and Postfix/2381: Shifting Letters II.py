# https://leetcode.com/problems/shifting-letters-ii/
# difficulty: medium
# topics: array, string, prefix sum

# problem:
# You are given a string s of lowercase English letters and a 2D integer array shifts where shifts[i] = [starti, endi, directioni]. For every i, shift the characters in s from the index starti to the index endi (inclusive) forward if directioni = 1, or shift the characters backward if directioni = 0.
# Shifting a character forward means replacing it with the next letter in the alphabet (wrapping around so that 'z' becomes 'a'). Similarly, shifting a character backward means replacing it with the previous letter in the alphabet (wrapping around so that 'a' becomes 'z').
# Return the final string after all such shifts to s are applied.

class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        n = len(s)
        indexChange = [0] * (n+1)
        ans = []
        for start, end, direction in shifts:
            multiplier = 1 if direction == 1 else -1
            indexChange[start] += 1*multiplier
            indexChange[end+1] -= 1*multiplier

        def newCharacter(c, d):
            return chr(ord('a') + (ord(c) - ord('a') + d) % 26)

        totalChange = 0
        for i in range(n):
            totalChange += indexChange[i]
            ans.append(newCharacter(s[i], totalChange))
        return ''.join(ans)
# time complexity: O(n + m), where n is length of s and m is length of shifts
# space complexity: O(n)

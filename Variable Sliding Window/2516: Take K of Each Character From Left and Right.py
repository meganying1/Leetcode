# https://leetcode.com/problems/take-k-of-each-character-from-left-and-right/
# difficulty: medium
# topics: hash table, string, sliding window

# problem:
# You are given a string s consisting of the characters 'a', 'b', and 'c' and a non-negative integer k. Each minute, you may take either the leftmost character of s, or the rightmost character of s.
# Return the minimum number of minutes needed for you to take at least k of each character, or return -1 if it is not possible to take k of each character.

class Solution:
    def takeCharacters(self, s: str, k: int) -> int:
        counts = [0] * 3
        for c in s: counts[ord(c)-ord("a")] += 1
        for i in range(3):
            if counts[i] < k: return -1
        n = len(s)
        windowCounts = [0] * 3
        start = end = largest = 0
        while end < n:
            windowCounts[ord(s[end])-ord("a")] += 1
            while start <= end and ((counts[0] - windowCounts[0] < k) or (counts[1] - windowCounts[1] < k) or (counts[2] - windowCounts[2] < k)):
                windowCounts[ord(s[start])-ord("a")] -= 1
                start += 1
            largest = max(largest, end-start+1)
            end += 1
        return n - largest
# time complexity: O(n)
# space complexity: O(1)

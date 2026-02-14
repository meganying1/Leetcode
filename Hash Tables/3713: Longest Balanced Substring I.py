# https://leetcode.com/problems/longest-balanced-substring-i/
# difficulty: medium
# topics: hash table, string, counting, enumeration

# description:
# You are given a string s consisting of lowercase English letters.
# A substring of s is called balanced if all distinct characters in the substring appear the same number of times.
# Return the length of the longest balanced substring of s.

class Solution:
    def longestBalanced(self, s: str) -> int:
        n, ans = len(s), 0
        for i in range(n):
            counts = defaultdict(int)
            for j in range(i, n):
                counts[s[j]] += 1
                if len(set(counts.values())) == 1: ans = max(ans, j-i+1)
        return ans
# time complexity: O(26n^2)
  # outer for loop runs n times and inner for loop runs n times
  # each inner iteration takes O(26) time because we iterate over each key in counts, which could be up to 26 characters
# space complexity: O(26)

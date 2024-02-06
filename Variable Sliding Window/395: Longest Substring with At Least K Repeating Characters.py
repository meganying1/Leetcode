# https://leetcode.com/problems/longest-substring-with-at-least-k-repeating-characters/description/
# difficulty: medium
# topics: hash table, string, divide and conquer, sliding window

# problem:
# Given a string s and an integer k, return the length of the longest substring of s such that the frequency of each character in this substring is greater than or equal to k.
# if no such substring exists, return 0.

class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        length = len(s)
        if length < k: return 0
        totalCounts = Counter(s)
        maxUnique = len(totalCounts)
        ans = 0
        for numUnique in range(1, maxUnique+1):
            if numUnique * k > length: break
            start, end = 0, k*numUnique - 1
            currCounts = Counter(s[i] for i in range(end+1))
            currUnique = len(currCounts)
            matches = sum(1 for c in currCounts if currCounts[c] >= k)
            while end < length:
                if matches == currUnique: ans = max(ans, end-start+1)
                while currUnique > numUnique:
                    currCounts[s[start]] -= 1
                    if currCounts[s[start]] == 0: currUnique -= 1
                    if currCounts[s[start]] == k-1: matches -= 1
                    start += 1
                if currUnique <= numUnique:
                    end += 1
                    if end == length: break
                    currCounts[s[end]] += 1
                    if currCounts[s[end]] == 1: currUnique += 1
                    if currCounts[s[end]] == k: matches += 1
        return ans

# when a question asks you "what is the longest substring where each character has >= k occurrences," first two questions should be:
#   can I check if a substring of a certain size works? is there any way to break down which sizes I should try?
#   how many characters can I include in a substring?

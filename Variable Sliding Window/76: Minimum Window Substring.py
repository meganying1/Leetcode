# https://leetcode.com/problems/minimum-window-substring/description/
# difficulty: hard
# topics: hash table, string, sliding window

# problem:
# Given two strings s and t of lengths m and n respectively, return the minimum window  substring of s such that every character in t (including duplicates) is included in the window. If there is no such substring, return the empty string "".
# The testcases will be generated such that the answer is unique.

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        sLen, tLen = len(s), len(t)
        if sLen < tLen: return ""
        tCount = Counter(t)
        sCount = Counter(s[i] for i in range(tLen))
        matches = sum(min(sCount[c], tCount[c]) for c in tCount)
        minLen = float("inf")
        ans = ""
        start, end = 0, tLen-1
        while end < sLen:
            if matches == tLen:
                if end-start+1 < minLen:
                    minLen = end-start+1
                    ans = s[start:end+1]
                else:
                    sCount[s[start]] -= 1
                    if sCount[s[start]]+1 == tCount[s[start]]: matches -= 1
                    start += 1
            elif matches < tLen:
                while matches < tLen:
                    end += 1
                    if end == sLen: break
                    sCount[s[end]] += 1
                    if sCount[s[end]] <= tCount[s[end]]: matches += 1
            else:
                while matches > tLen:
                    sCount[s[start]] -= 1
                    if sCount[s[start]]+1 == tCount[s[start]]: matches -= 1
                    start += 1
        return ans

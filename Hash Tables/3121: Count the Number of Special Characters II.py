# https://leetcode.com/problems/count-the-number-of-special-characters-ii/
# difficulty: medium
# topics: hash table, string

# description:
# You are given a string word. A letter c is called special if it appears both in lowercase and uppercase in word, and every lowercase occurrence of c appears before the first uppercase occurrence of c.
# Return the number of special letters in word.

class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        ans = 0
        upperIdx, lowerIdx = {}, {}
        for i, x in enumerate(word):
            if x.isupper() and x not in upperIdx: upperIdx[x] = i
            elif x.islower(): lowerIdx[x] = i
        for x in lowerIdx:
            upperX = x.upper()
            if upperX in upperIdx and upperIdx[upperX] > lowerIdx[x]: ans += 1
        return ans
# time complexity: O(n + 26)
# space complexity: O(26)

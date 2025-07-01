# https://leetcode.com/problems/find-the-original-typed-string-i/
# topics: string
# difficulty: easy

# problem:
# Alice is attempting to type a specific string on her computer. However, she tends to be clumsy and may press a key for too long, resulting in a character being typed multiple times.
# Although Alice tried to focus on her typing, she is aware that she may still have done this at most once.
# You are given a string word, which represents the final output displayed on Alice's screen.
# Return the total number of possible original strings that Alice might have intended to type.

class Solution:
    def possibleStringCount(self, word: str) -> int:
        n = len(word)
        l = r = 0
        ans = 1
        while r < n:
            while r < n and word[r] == word[l]:
                r += 1
            ans += r - l - 1
            l = r
        return ans
# time complexity: O(n)
# space complexity: O(1)

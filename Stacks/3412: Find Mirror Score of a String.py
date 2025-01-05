# https://leetcode.com/problems/find-mirror-score-of-a-string/
# difficulty: medium

# problem:
# You are given a string s.
# We define the mirror of a letter in the English alphabet as its corresponding letter when the alphabet is reversed. For example, the mirror of 'a' is 'z', and the mirror of 'y' is 'b'.
# Initially, all characters in the string s are unmarked.
# You start with a score of 0, and you perform the following process on the string s:
# Iterate through the string from left to right.
# At each index i, find the closest unmarked index j such that j < i and s[j] is the mirror of s[i]. Then, mark both indices i and j, and add the value i - j to the total score.
# If no such index j exists for the index i, move on to the next index without making any changes.
# Return the total score at the end of the process.

class Solution:
    def calculateScore(self, s: str) -> int:
        score = 0
        n = len(s)
        charToInd = defaultdict(list)
        reverse = 'zyxwvutsrqponmlkjihgfedcba'

        def getMirror(c):
            return reverse[ord(c) - ord('a')]
            
        for i in range(n):
            mirror = getMirror(s[i])
            if charToInd[mirror] != []:
                score += i - charToInd[mirror].pop()
            else:
                charToInd[s[i]].append(i)
        return score
# time complexity: O(n)
# space complexity: O(n)

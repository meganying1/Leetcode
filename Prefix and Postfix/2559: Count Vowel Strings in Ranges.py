# https://leetcode.com/problems/count-vowel-strings-in-ranges/
# difficulty: medium
# topics: array, string, prefix sum

# problem:
# You are given a 0-indexed array of strings words and a 2D array of integers queries.
# Each query queries[i] = [li, ri] asks us to find the number of strings present in the range li to ri (both inclusive) of words that start and end with a vowel.
# Return an array ans of size queries.length, where ans[i] is the answer to the ith query.
# Note that the vowel letters are 'a', 'e', 'i', 'o', and 'u'.

class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        n = len(words)
        prefix = [0] * (n+1)
        vowels = {'a', 'e', 'i', 'o', 'u'}
        ans = []
        for i in range(n):
            if words[i][0] in vowels and words[i][-1] in vowels: prefix[i+1] += 1
            prefix[i+1] += prefix[i]
        for l, r in queries:
            ans.append(prefix[r+1]-prefix[l])
        return ans
# time complexity: O(n+m), where n is length of words and m is length of queries
# space complexity: O (n)

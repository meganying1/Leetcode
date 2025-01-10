# https://leetcode.com/problems/word-subsets/
# difficulty: medium
# topics: array, hash table, string

# problems:
# You are given two string arrays words1 and words2.
# A string b is a subset of string a if every letter in b occurs in a including multiplicity.
#   For example, "wrr" is a subset of "warrior" but is not a subset of "world".
# A string a from words1 is universal if for every string b in words2, b is a subset of a.
# Return an array of all the universal strings in words1. You may return the answer in any order.

class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        ans = []
        neededCounts = defaultdict(int)
        for str2 in words2:
            counts2 = Counter(str2)
            for c in counts2:
                neededCounts[c] = max(neededCounts[c], counts2[c])

        def isUniversal(s):
            counts1 = Counter(s)
            for c in neededCounts:
                if neededCounts[c] > counts1[c]: return False
            return True

        for str1 in words1:
            if isUniversal(str1): ans.append(str1)
        return ans
# time complexity: O(n + m), where n is total number of characters in words1 and k is total number of characters in words2
#   creating neededCounts dictionary requires iterating over all characters in words2, which takes O(m) time
#   checking if each string in words1 is universal requires iterating over all characters in words1, which takes O(n) time
# space complexity: O(n + m)

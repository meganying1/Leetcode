# https://leetcode.com/problems/check-if-strings-can-be-made-equal-with-operations-ii/
# difficulty: medium
# topics: hash table, string, sorting

# description:
# You are given two strings s1 and s2, both of length n, consisting of lowercase English letters.
# You can apply the following operation on any of the two strings any number of times:
#   Choose any two indices i and j such that i < j and the difference j - i is even, then swap the two characters at those indices in the string.
# Return true if you can make the strings s1 and s2 equal, and false otherwise.

# more concise:
class Solution:
    def checkStrings(self, s1: str, s2: str) -> bool:
       return Counter(s1[::2]) == Counter(s2[::2]) and Counter(s1[1::2]) == Counter(s2[1::2])
# time complexity: O(n), where n is len(s1)
# space complexity: O(n)

"""
class Solution:
    def checkStrings(self, s1: str, s2: str) -> bool:
        odds1, odds2, evens1, evens2 = defaultdict(int), defaultdict(int), defaultdict(int), defaultdict(int)
        for i in range(len(s1)):
            if i % 2 == 0:
                evens1[s1[i]] += 1
                evens2[s2[i]] += 1
            else:
                odds1[s1[i]] += 1
                odds2[s2[i]] += 1
        return evens1 == evens2 and odds1 == odds2
"""
# time complexity: O(n), where n is len(s1)
# space complexity: O(n)

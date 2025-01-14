# https://leetcode.com/problems/find-the-prefix-common-array-of-two-arrays
# difficulty: medium
# topics: array, hash table, bit manipulation

# problem:
# You are given two 0-indexed integer permutations A and B of length n.
# A prefix common array of A and B is an array C such that C[i] is equal to the count of numbers that are present at or before the index i in both A and B.
# Return the prefix common array of A and B.
# A sequence of n integers is called a permutation if it contains all integers from 1 to n exactly once.

class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        n = len(A)
        ans = [0] * n
        counts = defaultdict(int)
        common = 0
        for i in range(n):
            counts[A[i]] += 1
            if counts[A[i]] == 2: common += 1
            counts[B[i]] += 1
            if counts[B[i]] == 2: common += 1
            ans[i] = common
        return ans
# time complexity: O(n)
# space complexity: O(n)

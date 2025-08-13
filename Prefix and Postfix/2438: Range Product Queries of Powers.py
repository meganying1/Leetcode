# https://leetcode.com/problems/range-product-queries-of-powers
# topics: array, bit manipulation, prefix sum
# difficulty: medium

# problem:
# Given a positive integer n, there exists a 0-indexed array called powers, composed of the minimum number of powers of 2 that sum to n. The array is sorted in non-decreasing order, and there is only one way to form the array.
# You are also given a 0-indexed 2D integer array queries, where queries[i] = [lefti, righti]. Each queries[i] represents a query where you have to find the product of all powers[j] with lefti <= j <= righti.
# Return an array answers, equal in length to queries, where answers[i] is the answer to the ith query. Since the answer to the ith query may be too large, each answers[i] should be returned modulo 109 + 7.

class Solution:
    def productQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        powers, pos = [1], 1
        mod = 10 **9 + 7
        ans = []
        while n > 0:
            if n & 1 == 1: powers.append(pos)
            n >>= 1
            pos *= 2
        for i in range(1, len(powers)):
            powers[i] *= powers[i-1]
        for l, r in queries:
            ans.append((powers[r+1] // powers[l]) % mod)
        return ans
# time complexity: O(logn + q), where q is len(q)
#   it takes O(logn) time to create powers and preprocess our array because iterating over all the bits in n takes O(logn) time
# space complexity: O(logn)

"""
class Solution:
    def productQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        binNum = str(bin(n))[2:]
        length = len(binNum)
        powers = [1]
        mod = 10 **9 + 7
        ans = []
        for i in range(length-1, -1, -1):
            if binNum[i] == '1': powers.append(2 ** (length-i-1))
        for i in range(1, len(powers)):
            powers[i] *= powers[i-1]
        for l, r in queries:
            ans.append((powers[r+1] // powers[l]) % mod)
        return ans
"""
# time complexity: O(logn + q), where q is len(q)
#   it takes O(logn) time to create binNum, create powers, and preprocess our array because iterating over all the bits in n takes O(logn) time
# space complexity: O(logn)

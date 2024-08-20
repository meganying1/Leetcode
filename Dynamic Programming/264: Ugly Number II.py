# https://leetcode.com/problems/ugly-number-ii/description/
# difficulty: medium
# topics: hash table, math, dynamic programming, heap (priority queue)

# problem:
# An ugly number is a positive integer whose prime factors are limited to 2, 3, and 5.
# Given an integer n, return the nth ugly number.

class Solution(object):
    def nthUglyNumber(self, n):
        dp = [0] * n
        dp[0] = 1
        curr2 = curr3 = curr5 = 0
        next2, next3, next5 = 2, 3, 5
        for i in range(1, n):
            nextNum = min(next2, next3, next5)
            dp[i] = nextNum
            if nextNum == next2:
                curr2 += 1
                next2 = dp[curr2] * 2
            if nextNum == next3:
                curr3 += 1
                next3 = dp[curr3] * 3
            if nextNum == next5:
                curr5 += 1
                next5 = dp[curr5] * 5
        return dp[-1]
# dynamic programming solution
# time complexity: O(n)
# space complexity: O(n)

"""
class Solution(object):
    def nthUglyNumber(self, n):
        if n == 1: return 1
        heap, popped, added = [], 0, set()
        heapq.heappush(heap, 1)
        added.add(1)
        for _ in range(n):
            curr = heapq.heappop(heap)
            popped += 1
            for factor in (2, 3, 5):
                if curr*factor in added: continue
                heapq.heappush(heap, curr*factor)
                added.add(curr*factor)
        return curr
"""
# heap solution
# time complexity: O(n*logn)
#   heappush and heappop take O(logn) time, and we have n of these operations
# space complexity: O(m)
#   heap and set store m unique ugly numbers

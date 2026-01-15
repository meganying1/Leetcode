# https://leetcode.com/problems/separate-squares-i/
# difficulty: medium
# topics: array, binary search

# description:
# You are given a 2D integer array squares. Each squares[i] = [xi, yi, li] represents the coordinates of the bottom-left point and the side length of a square parallel to the x-axis.
# Find the minimum y-coordinate value of a horizontal line such that the total area of the squares above the line equals the total area of the squares below the line.
# Answers within 10-5 of the actual answer will be accepted.
# Note: Squares may overlap. Overlapping areas should be counted multiple times.

class Solution:
    def separateSquares(self, squares: List[List[int]]) -> float:
        lo, hi, total = float('inf'), -float('inf'), 0
        for _, y, l in squares:
            total += l * l
            lo = min(lo, y)
            hi = max(hi, y + l)
        while hi - lo > (10 ** -5):
            mid = (lo + hi) / 2
            curr = 0
            for _, y, l in squares:
                curr += l * max(0, min(l, mid - y))
            if curr >= total / 2: hi = mid
            else: lo = mid
        return lo
# time complexity: O(nlogk), where k = hi - lo
#   first for loop runs n times
#   while loop runs logk times
#   second for loop runs n times
# space complexity: O(1)

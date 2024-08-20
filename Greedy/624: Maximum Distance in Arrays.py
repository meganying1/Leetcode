# https://leetcode.com/problems/maximum-distance-in-arrays
# difficulty: medium
# topics: array, greedy

# problem:
# You are given m arrays, where each array is sorted in ascending order.
# You can pick up two integers from two different arrays (each array picks one) and calculate the distance. We define the distance between two integers a and b to be their absolute difference |a - b|.
# Return the maximum distance.

class Solution(object):
    def maxDistance(self, arrays):
        m = len(arrays)
        ans = 0
        currMin, currMax = arrays[0][0], arrays[0][-1]
        for i in range(1, m):
            ans = max(ans, arrays[i][-1]-currMin, currMax-arrays[i][0])
            currMin = min(currMin, arrays[i][0])
            currMax = max(currMax, arrays[i][-1])
        return ans
# we know that m <= 10*5, so goal time complexity is O(m)
# time complexity: O(m)
# space complexity: O(1)

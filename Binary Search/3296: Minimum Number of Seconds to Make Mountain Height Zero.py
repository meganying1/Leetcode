# https://leetcode.com/problems/minimum-number-of-seconds-to-make-mountain-height-zero/
# difficulty: medium
# topics: array, math, binary search, greedy, heap (priority queue)

# description:
# You are given an integer mountainHeight denoting the height of a mountain.
# You are also given an integer array workerTimes representing the work time of workers in seconds.
# The workers work simultaneously to reduce the height of the mountain. For worker i:
  # To decrease the mountain's height by x, it takes workerTimes[i] + workerTimes[i] * 2 + ... + workerTimes[i] * x seconds. For example:
  # To reduce the height of the mountain by 1, it takes workerTimes[i] seconds.
  # To reduce the height of the mountain by 2, it takes workerTimes[i] + workerTimes[i] * 2 seconds, and so on.
# Return an integer representing the minimum number of seconds required for the workers to make the height of the mountain 0.

class Solution:
    def minNumberOfSeconds(self, mountainHeight: int, workerTimes: List[int]) -> int:
        n = len(workerTimes)
        
        def canReduce(seconds):
            totalHeight = 0
            for t in workerTimes:
                work = seconds // t
                k = int((-1 + ((1 + work * 8) ** 0.5)) / 2)
                totalHeight += k
            return totalHeight >= mountainHeight

        lo = hi = 0
        minTime = min(workerTimes)
        for i in range(mountainHeight):
            hi += minTime * (i + 1)
        ans = hi
        while lo <= hi:
            mid = (hi + lo) // 2
            if canReduce(mid):
                ans = mid
                hi = mid - 1
            else:
                lo = mid + 1
        return ans

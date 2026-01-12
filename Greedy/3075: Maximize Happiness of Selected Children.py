# https://leetcode.com/problems/maximize-happiness-of-selected-children/
# difficulty: medium
# topics: array, greedy, sorting

# description:
# You are given an array happiness of length n, and a positive integer k.
# There are n children standing in a queue, where the ith child has happiness value happiness[i]. You want to select k children from these n children in k turns.
# In each turn, when you select a child, the happiness value of all the children that have not been selected till now decreases by 1. Note that the happiness value cannot become negative and gets decremented only if it is positive.
# Return the maximum sum of the happiness values of the selected children you can achieve by selecting k children.

class Solution:
    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:
        n = len(happiness)
        happiness.sort()
        ans = 0
        for i in range(k):
            ans += max(0, happiness[n-i-1] - i)
        return ans
# time complexity: O(nlogn)
# space complexity: O(sort)

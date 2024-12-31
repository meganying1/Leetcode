# https://leetcode.com/problems/minimum-cost-for-tickets/
# difficulty: medium
# topics: array, dynamic programming

# problem:
# You have planned some train traveling one year in advance. The days of the year in which you will travel are given as an integer array days. Each day is an integer from 1 to 365.
# Train tickets are sold in three different ways:
#   a 1-day pass is sold for costs[0] dollars,
#   a 7-day pass is sold for costs[1] dollars, and
#   a 30-day pass is sold for costs[2] dollars.
# The passes allow that many days of consecutive travel.
# For example, if we get a 7-day pass on day 2, then we can travel for 7 days: 2, 3, 4, 5, 6, 7, and 8.
# Return the minimum number of dollars you need to travel every day in the given list of days.

class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        dp = [0] * (days[-1] + 1)
        daysSet = set(days)
        for day in range(1, days[-1]+1):
            if day not in daysSet: dp[day] = dp[day-1]
            else: dp[day] = min(dp[day-1]+costs[0], dp[max(0, day-7)]+costs[1], dp[max(0, day-30)]+costs[2])
        return dp[-1]
# bottom-up dynamic programming solution
# time complexity: O(k), where k is last day we need to travel
# space complexity: O(k)

class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        cache = [None] * (days[-1] + 1)
        daysSet = set(days)
        
        def dp(day):
            if day > days[-1]: return 0
            if cache[day] != None: return cache[day]
            if day not in daysSet: ans = dp(day+1)
            else: ans = min(dp(day+1)+costs[0], dp(day+7)+costs[1], dp(day+30)+costs[2])
            cache[day] = ans
            return ans
        
        return dp(1)
# top-down dynamic programming solution #2
# time complexity: O(k), where k is last day we need to travel
# space complexity: O(k)

class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        n = len(days)
        cache = [None] * (n)
        
        def dp(i):
            if i == n: return 0
            if cache[i] != None: return cache[i]
            onePass = dp(bisect_left(days, days[i]+1)) + costs[0]
            sevenPass = dp(bisect_left(days, days[i]+7)) + costs[1]
            thirtyPass = dp(bisect_left(days, days[i]+30)) + costs[2]
            ans = min(onePass, sevenPass, thirtyPass)
            cache[i] = ans
            return ans
        
        return dp(0)
# top-down dynamic programming solution #1
# time complexity: O(nlogn), where n is length of days
# space complexity: O(n)

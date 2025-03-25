# https://leetcode.com/problems/count-days-without-meetings
# difficulty: medium
# topics: array, sorting

# problem:
# You are given a positive integer days representing the total number of days an employee is available for work (starting from day 1). You are also given a 2D array meetings of size n where, meetings[i] = [start_i, end_i] represents the starting and ending days of meeting i (inclusive).
# Return the count of days when the employee is available for work but no meetings are scheduled.
# Note: The meetings may overlap.

class Solution:
    def countDays(self, days: int, meetings: List[List[int]]) -> int:
        ans = 0
        meetings.sort()
        latest = 0
        for start, end in meetings:
            ans += max(0, start-latest-1)
            latest = max(end, latest)
        return ans + days - latest
# time complexity: O(nlogn)
# space complexity: O(1)

'''
class Solution:
    def countDays(self, days: int, meetings: List[List[int]]) -> int:
        ans = 0
        meetings.sort()
        merged = [meetings[0]]
        for i in range(1, len(meetings)):
            if merged[-1][1] >= meetings[i][0]:
                if merged[-1][1] <= meetings[i][1]:
                    merged[-1][1] = meetings[i][1]
            else: merged.append(meetings[i])
        for i in range(1, len(merged)):
            ans += merged[i][0] - merged[i-1][1] - 1
        return ans + (merged[0][0] - 1) + (days - merged[-1][1])
'''
# time complexity: O(nlogn)
# space complexity: O(n)

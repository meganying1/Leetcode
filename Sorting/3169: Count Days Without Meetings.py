# https://leetcode.com/problems/count-days-without-meetings
# difficulty: medium
# topics: array, sorting

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

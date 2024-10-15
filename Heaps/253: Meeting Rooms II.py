# https://leetcode.com/problems/meeting-rooms-ii/
# difficulty: medium
# topics: array, greedy, two pointers, prefix sum, sorting, heap (priority queue)

# Given an array of meeting time intervals consisting of start and end times [[s1,e1],[s2,e2],...] (si < ei), find the minimum number of conference rooms required.

# heap solution
class Solution:
    def minMeetingRooms(self, meetings: List[List[int]]) -> int:
        meetings.sort()
        rooms = []
        heapq.heappush(rooms, meetings[0][1])
        for start, end in meetings[1:]:
            if rooms[0] <= start:
                heapq.heappop(rooms)
            heapq.heappush(rooms, end)
        return len(rooms)
# time complexity: O(nlogn)
# space complexity: O(n)

# top of heap is the meeting that will end soonest, and we can remove it if it ends before the next meeting starts
# the size of the heap at the end is the minimum rooms needed

# two pointers solution
class Solution:
    def minMeetingRooms(self, meetings: List[List[int]]) -> int:
        n = len(meetings)
        start, end = [x[0] for x in meetings], [x[1] for x in meetings]
        start.sort()
        end.sort()
        startPtr = endPtr = 0
        ans = 0
        while startPtr < n and endPtr < n:
            if start[startPtr] < end[endPtr]: ans += 1
            else: endPtr += 1
            startPtr += 1
        return ans
# time complexity: O(nlogn)
# space complexity: O(n)

# when we increment start pointer, a new meeting has begun and we need another room
# when we increment end pointer, a meeting has ended and a room becomes available for use

# https://leetcode.com/problems/my-calendar-i/
# topics: array, binary search, design, segment tree, ordered set
# difficulty: medium

# problem:
# You are implementing a program to use as your calendar. We can add a new event if adding the event will not cause a double booking.
# A double booking happens when two events have some non-empty intersection (i.e., some moment is common to both events.).
# The event can be represented as a pair of integers startTime and endTime that represents a booking on the half-open interval [startTime, endTime), the range of real numbers x such that startTime <= x < endTime.
# Implement the MyCalendar class:
#   MyCalendar() Initializes the calendar object.
#   boolean book(int startTime, int endTime) Returns true if the event can be added to the calendar successfully without causing a double booking. Otherwise, return false and do not add the event to the calendar.

class MyCalendar:

    def __init__(self):
        self.calendar = SortedList()

    def book(self, startTime: int, endTime: int) -> bool:
        i = bisect_left(self.calendar, (startTime, endTime))
        if (i != len(self.calendar) and self.calendar[i][0] < endTime) or (i != 0 and self.calendar[i-1][1] > startTime):
            return False
        self.calendar.add((startTime, endTime))
        return True 


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(startTime,endTime)

# time complexity: O(nlogn), where n is number of events booked
#   binary search takes O(logn) time and insertion into sorted list takes O(logn) time
# space complexity: O(n)

"""
class MyCalendar:

    def __init__(self):
        self.calendar = []

    def book(self, startTime: int, endTime: int) -> bool:
        i = bisect_left(self.calendar, (startTime, endTime))
        if (i != len(self.calendar) and self.calendar[i][0] < endTime) or (i != 0 and self.calendar[i-1][1] > startTime):
            return False
        self.calendar.insert(i, (startTime, endTime))
        return True 
"""
# time complexity: O(n^2), where n is the number of events booked
#   binary search takes O(logn) time and insertion takes O(n) time
# space complexity: O(n)

# can use sorted list to speed up

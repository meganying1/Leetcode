# https://leetcode.com/problems/time-based-key-value-store/
# difficulty: medium
# topics: hash table, string, binary search, design

# description:
# Design a time-based key-value data structure that can store multiple values for the same key at different time stamps and retrieve the key's value at a certain timestamp.
# Implement the TimeMap class:
#   TimeMap() Initializes the object of the data structure.
#   void set(String key, String value, int timestamp) Stores the key key with the value value at the given time timestamp.
#   String get(String key, int timestamp) Returns a value such that set was called previously, with timestamp_prev <= timestamp. If there are multiple such values, it returns the value associated with the largest timestamp_prev. If there are no values, it returns "".

class TimeMap:

    def __init__(self):
        self.keyDict = defaultdict()

    def set(self, key: str, value: str, timestamp: int) -> None:
        timeValue = (timestamp, value)
        if key not in self.keyDict: self.keyDict[key] = []
        self.keyDict[key].append(timeValue)

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.keyDict: return ""
        valueList = self.keyDict[key]
        if valueList[0][0] > timestamp: return ""
        elif valueList[-1][0] < timestamp: return valueList[-1][1]
        i = bisect_left(valueList, (timestamp, ''))
        if valueList[i][0] > timestamp: i -= 1
        return valueList[i][1]

# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)

# time complexity:
#   __init__: O(1)
#   set: O(1)
#   get: O(logn)
# space complexity: O(n)

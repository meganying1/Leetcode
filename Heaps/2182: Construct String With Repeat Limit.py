# https://leetcode.com/problems/construct-string-with-repeat-limit/
# difficulty: medium
# topics: hash table, string, greedy, heap (priority queue), counting

# problem:
# You are given a string s and an integer repeatLimit. Construct a new string repeatLimitedString using the characters of s such that no letter appears more than repeatLimit times in a row. You do not have to use all characters from s.
# Return the lexicographically largest repeatLimitedString possible.
# A string a is lexicographically larger than a string b if in the first position where a and b differ, string a has a letter that appears later in the alphabet than the corresponding letter in b. If the first min(a.length, b.length) characters do not differ, then the longer string is the lexicographically larger one.

class Solution:
    def repeatLimitedString(self, s: str, repeatLimit: int) -> str:
        ans, counts = [], Counter(s)
        maxHeap = [(-ord(c), counts[c]) for c in counts]
        heapq.heapify(maxHeap)
        while maxHeap:
            highestChar, highestCount = heapq.heappop(maxHeap)
            for _ in range(min(highestCount, repeatLimit)):
                ans.append(chr(-highestChar))
            if maxHeap and highestCount > repeatLimit:
                nextChar, nextCount = heapq.heappop(maxHeap)
                ans.append(chr(-nextChar))
                if nextCount > 1:
                    heapq.heappush(maxHeap, (nextChar, nextCount-1))
                heapq.heappush(maxHeap, (highestChar, highestCount-repeatLimit))
        return "".join(ans)
# k represent number of unique characters
# time complexity: O(nlogk)
#   it takes O(n) time to initialize maxHeap and run heapify
#   size of heap is k
#   while loop runs n times in worst case scenario
#   while loop takes O(nlogk) time
# space complexity: O(k)

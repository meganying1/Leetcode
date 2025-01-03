# https://leetcode.com/problems/maximum-average-pass-ratio/
# difficulty: medium
# topics: array, greedy, heap (priority queue)

# problem:
# There is a school that has classes of students and each class will be having a final exam. You are given a 2D integer array classes, where classes[i] = [passi, totali]. You know beforehand that in the ith class, there are totali total students, but only passi number of students will pass the exam.
# You are also given an integer extraStudents. There are another extraStudents brilliant students that are guaranteed to pass the exam of any class they are assigned to. You want to assign each of the extraStudents students to a class in a way that maximizes the average pass ratio across all the classes.
# The pass ratio of a class is equal to the number of students of the class that will pass the exam divided by the total number of students of the class. The average pass ratio is the sum of pass ratios of all the classes divided by the number of the classes.
# Return the maximum possible average pass ratio after assigning the extraStudents students. Answers within 10-5 of the actual answer will be accepted.

class Solution:
    def maxAverageRatio(self, classes: List[List[int]], extraStudents: int) -> float:
        maxHeap = []
        ans = 0
        for passCount, totalCount in classes:
            currRatio = passCount/totalCount
            addedRatio = (passCount+1)/(totalCount+1)
            maxHeap.append((-(addedRatio-currRatio), passCount, totalCount))
        heapq.heapify(maxHeap)
        for _ in range(extraStudents):
            passChange, passCount, totalCount = heapq.heappop(maxHeap)
            totalCount += 1
            passCount += 1
            currRatio = passCount/totalCount
            addedRatio = (passCount+1)/(totalCount+1)
            heapq.heappush(maxHeap, (-(addedRatio-currRatio), passCount, totalCount))
        for passChange, passCount, totalCount in maxHeap:
            ans += passCount/totalCount
        return ans / len(classes)
# time complexity: O(klogn + n), where k is number of extra students and n is number of classes
#   it takes O(n) time to add all elements to maxHeap and heapify
#   when adding extra students, we remove and insert from the max heap k times, which each take O(logn) time
# space complexity: O(n)

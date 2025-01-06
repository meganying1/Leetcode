# https://leetcode.com/problems/minimum-number-of-operations-to-move-all-balls-to-each-box/
# difficulty: medium
# topics: array, string, prefix sum

# problem: 
# You have n boxes. You are given a binary string boxes of length n, where boxes[i] is '0' if the ith box is empty, and '1' if it contains one ball.
# In one operation, you can move one ball from a box to an adjacent box. Box i is adjacent to box j if abs(i - j) == 1. Note that after doing so, there may be more than one ball in some boxes.
# Return an array answer of size n, where answer[i] is the minimum number of operations needed to move all the balls to the ith box.
# Each answer[i] is calculated considering the initial state of the boxes.

class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        n = len(boxes)
        ans = [0] * n
        leftBalls = rightBalls = 0
        if boxes[0] == '1': leftBalls = 1
        for i in range(1, n):
            if boxes[i] == '1':
                rightBalls += 1
                ans[0] += i
        for i in range(1, n):
            ans[i] = ans[i-1] + leftBalls - rightBalls
            if boxes[i] == '1': 
                leftBalls += 1
                rightBalls -= 1
        return ans
# time complexity: O(n)
# space complexity: O(1)

class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        n = len(boxes)
        ans = [0] * n
        balls = [0] * n
        if boxes[0] == '1':
            balls[0] = 1
        for i in range(1, n):
            if boxes[i] == '1':
                balls[i] += 1
                ans[0] += i
            balls[i] += balls[i-1]
        for i in range(1, n):
            ans[i] = ans[i-1] + (balls[i-1]) - (balls[-1]-balls[i-1])
        return ans
# time complexity: O(n)
# space complexity: O(n)
# can store number of balls to left and number of balls to right in order to optimize space

class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        n = len(boxes)
        ballBoxes = []
        ans = [0] * n
        for i in range(n):
            if boxes[i] == '1': ballBoxes.append(i)
        for i in range(n):
            for j in ballBoxes:
                ans[i] += abs(i-j)
        return ans
# time complexity: O(n^2)
# space complexity: O(n)
# can pre-process array to optimize time complexity

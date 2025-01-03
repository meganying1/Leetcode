# https://leetcode.com/problems/find-score-of-an-array-after-marking-all-elements/
# difficulty: medium
# topics: array, hash table, sorting, heap (priority queue), simulation

# problem:
#You are given an array nums consisting of positive integers.
# Starting with score = 0, apply the following algorithm:
# Choose the smallest integer of the array that is not marked. If there is a tie, choose the one with the smallest index.
#   Add the value of the chosen integer to score.
#   Mark the chosen element and its two adjacent elements if they exist.
#   Repeat until all the array elements are marked.
# Return the score you get after applying the above algorithm.

# stack solution:
class Solution:
    def findScore(self, nums: List[int]) -> int:
        n = len(nums)
        ans = i = 0
        stack = []
        for i in range(n):
            if not stack or nums[i] < stack[-1]:
                stack.append(nums[i])
                continue
            while stack:
                ans += stack.pop()
                if stack: stack.pop()
        while stack:
            ans += stack.pop()
            if stack: stack.pop()
        return ans
# time complexity: O(n)
# space complexity: O(n)
# idea: if number is less than its neighbors, we wil choose it and add it to our score, so we maintain a monotonically decreasing stack
# we can optimize space by getting rid of stack and using a poiner

# sorting solution
class Solution:
    def findScore(self, nums: List[int]) -> int:
        n = len(nums)
        ans = 0
        marked = [False] * n
        indexList = [(x, i) for i, x in enumerate(nums)]
        indexList.sort()
        for x, i in indexList:
            if marked[i]: continue
            ans += x
            marked[i] = True
            if i != 0: marked[i-1] = True
            if i != n-1: marked[i+1] = True
        return ans
# time complexity: O(nlogn)
# space complexity: O(n)

# heap solution
class Solution:
    def findScore(self, nums: List[int]) -> int:
        n = len(nums)
        ans = 0
        marked = [False] * n
        minHeap = [(x, i) for i, x in enumerate(nums)]
        heapq.heapify(minHeap)
        while minHeap:
            x, i = heapq.heappop(minHeap)
            if marked[i]: continue
            ans += x
            marked[i] = True
            if i != 0: marked[i-1] = True
            if i != n-1: marked[i+1] = True
        return ans
# time complexity: O(nlogn)
# space complexity: O(n)
# no need for heap since reordering doesn't occur whenever item is popped

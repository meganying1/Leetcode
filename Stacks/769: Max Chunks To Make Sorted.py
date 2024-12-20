# https://leetcode.com/problems/max-chunks-to-make-sorted/
# difficulty: medium
# topics: array, stack, greedy, sorting, monotonic stack

# problem:
# You are given an integer array arr of length n that represents a permutation of the integers in the range [0, n - 1].
# We split arr into some number of chunks (i.e., partitions), and individually sort each chunk. After concatenating them, the result should equal the sorted array.
# Return the largest number of chunks we can make to sort the array.

# space optimized solution:
class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        ans = 0
        maxSoFar = -1
        for i in range(len(arr)):
            maxSoFar = max(maxSoFar, arr[i])
            if maxSoFar == i: ans += 1
        return ans
# time complexity: O(n)
# space complexity O(1)

# stack solution:
class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        ans = 0
        stack = []
        for n in arr:
            if not stack or n > stack[-1]:
                stack.append(n)
            else:
                maxElem = stack[-1]
                while stack and n < stack[-1]:
                    stack.pop()
                stack.append(maxElem)
        return len(stack)
# time complexity: O(n)
# space complexity: O(n)

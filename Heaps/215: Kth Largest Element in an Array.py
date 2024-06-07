# https://leetcode.com/problems/kth-largest-element-in-an-array/
# difficulty: medium
# topics: array, divide and conquer, sorting, heap (priority queue), quickselect)

# problem:
# Given an integer array nums and an integer k, return the kth largest element in the array.
# Note that it is the kth largest element in the sorted order, not the kth distinct element.
# Can you solve it without sorting?

# heap solution
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = nums[:k]
        heapq.heapify(heap)
        for val in nums[k:]:
            if val > heap[0]: heapq.heappushpop(heap, val)
        return heap[0]
# time complexity: O(nlogk)
#     we push onto the heap n-k times in the worst case scenario and heappushpop takes O(logk) time where k is the size of the heap
# space complexity: O(n)
#     we have a heap of size k
#     we create an array of size n-k in the for loop

"""
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heapq.heapify(nums)
        for _ in range(len(nums)-k): heapq.heappop(nums)
        return nums[0]
"""

# quickselect solution (better solution)
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        
        def quickselect(arr, k):
            randInd = random.randint(0, len(arr)-1)
            randPivot = arr[randInd]
            left, right = [], []
            pivotCount = 0
            for num in arr:
                if num > randPivot: right.append(num)
                elif num < randPivot: left.append(num)
                else: pivotCount += 1
            n = len(right)
            if n >= k: return quickselect(right, k)
            elif n + pivotCount >= k: return randPivot
            return quickselect(left, k-n-pivotCount)

        return quickselect(nums, k)
# time complexity: O(n)
# space complexity: O(n)

"""
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        
        def quickselect(arr, k):
            randInd = random.randint(0, len(arr)-1)
            randPivot = arr[randInd]
            left, right = [], []
            leftCount, rightCount = 0, 0
            for num in arr:
                if num > randPivot: right.append(num)
                elif num < randPivot: left.append(num)
                else:
                    rand = random.randint(0, 1)
                    if rand == 1:
                        right.append(randPivot)
                        rightCount += 1
                    else:
                        left.append(randPivot)
                        leftCount += 1
            if rightCount == 0: left.remove(randPivot)
            elif leftCount == 0: right.remove(randPivot)
            else:
                rand = random.randint(0, 1)
                if rand == 1: left.remove(randPivot)
                else: right.remove(randPivot)
            n = len(right)
            if n >= k: return quickselect(right, k)
            elif n+1 == k: return randPivot
            return quickselect(left, k-n-1)

        return quickselect(nums, k)
"""
# time complexity: O(n)
# space complexity: O(n)
#     first iteration uses n space for left and right array, second uses n/2 space, etc.
#     n + n/2 + n/4 + ... reduces to n

# if we didn't use randomness:
#     time complexity: O(n^2)
#     space complexity: O(n^2)

"""
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        n = len(nums)
        
        def partition(l, r):
            x = nums[r]
            i = l
            for j in range(l, r):
                if nums[j] <= x:
                    nums[i], nums[j] = nums[j], nums[i]
                    i += 1
            nums[i], nums[r] = nums[r], nums[i]
            return i
        
        def helper(l, r):
            i = partition(l, r)
            if n-i == k: return nums[i]
            elif n-i > k: return helper(l+1, r)
            return helper(l, r-1)

        return helper(0, n-1)
"""
# time complexity: O(n^2)
#     always true for quick select without randomness
#     worst case scenario occurs when rightmost value in array is the smallest in the array and we call partition() n times
#     to fix: choose random index instead of r as pivot
# space complexity: O(n)

# if we used random pivot instead:
#     time complexity: O(n)
#         technically, worst case scenario is O(n^2), but it will only occur if we are very very unlucky
#         on average we process n elements the first iteration, then n/2, then n/4, then n/8, and so on, which simplifies to O(n)
#     space complexity: O(logn)
#         worst case scenario is O(n), but again will only occur if we are very very unlucky

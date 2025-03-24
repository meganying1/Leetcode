# https://leetcode.com/problems/sort-an-array/
# difficulty: medium
# topics: array, divide and conquer, sorting, heap (priority queue), merge sort, bucket sort, radix sort, counting sort

# problem:
# Given an array of integers nums, sort the array in ascending order and return it.
# You must solve the problem without using any built-in functions in O(nlog(n)) time complexity and with the smallest space complexity possible.

class Solution:
    def merge(self, list1, list2):
        len1, len2 = len(list1), len(list2)
        ind1, ind2 = 0, 0
        ans = []
        while ind1 < len1 and ind2 < len2:
            if list1[ind1] < list2[ind2]:
                ans.append(list1[ind1])
                ind1 += 1
            else: 
                ans.append(list2[ind2])
                ind2 += 1
        while ind1 < len1:
            ans.append(list1[ind1])
            ind1 += 1
        while ind2 < len2:
            ans.append(list2[ind2])
            ind2 += 1
        return ans

    def sortArray(self, nums: List[int]) -> List[int]:
        length = len(nums)
        if length == 1: return nums
        mid = length // 2
        return self.merge(self.sortArray(nums[:mid]), self.sortArray(nums[mid:]))
# time complexity: O(nlogn)
    # we have log(n) layers and each layer takes n time
# space complexity: O(n)
    # we first descend down left side of tree
        # first layer takes up n/2 space, second layer takes up n/4, third layer takes up n/8, etc.
        # all of this adds up to n space
    # we then descend down right side of tree
    # most space used at one point is n

    # can save space using l and r to track bounds of nums, doesn't affect space complexity
    # we know it is at least log(n) because that's the size of the callstack
# can also use an iterative approach using while loop, which results in space complexity of O(1)

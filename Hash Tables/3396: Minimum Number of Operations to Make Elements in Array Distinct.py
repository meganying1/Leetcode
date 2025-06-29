# https://leetcode.com/problems/minimum-number-of-operations-to-make-elements-in-array-distinct/
# topics: array, hash table
# difficulty: easy

# problem:
# You are given an integer array nums. You need to ensure that the elements in the array are distinct. To achieve this, you can perform the following operation any number of times:
#   Remove 3 elements from the beginning of the array. If the array has fewer than 3 elements, remove all remaining elements.
# Note that an empty array is considered to have distinct elements. Return the minimum number of operations needed to make the elements in the array distinct.

class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        n = len(nums)
        seen = set()
        distinct = 0
        for i in range(n-1, -1, -1):
            if nums[i] not in seen:
                distinct += 1
                seen.add(nums[i])
            else: break
        return math.ceil((n - distinct)/3)
# time complexity: O(n)
# space complexity: O(n)

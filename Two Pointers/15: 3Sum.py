# https://leetcode.com/problems/3sum/description/
# difficulty: medium
# topics: array, two pointers, sorting

# problem:
# Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.
# Notice that the solution set must not contain duplicate triplets.

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans = []
        length = len(nums)
        nums.sort()
        for i in range(length):
            if i != 0 and nums[i] == nums[i-1]: continue
            neededSum = -nums[i]
            j, k = i+1, length-1
            while j < k:
                currSum = nums[j] + nums[k]
                if currSum == neededSum:
                    ans.append((nums[i], nums[j], nums[k]))
                    j += 1 # you know you will need to increment j regardless
                    while j < length and nums[j] == nums[j-1]: j += 1 # increment j until it's unique
                elif currSum > neededSum: k -= 1
                else: j += 1
        return ans
# time complexity: O(n^2)
# space complexity:L O(sort)
#     sort() in python is O(n) space complexity, but don't assume and say that space complexity depends on the sort function

"""
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans = set()
        length = len(nums)
        nums.sort()
        for i in range(length):
            if i != 0 and nums[i] == nums[i-1]: continue
            neededSum = -nums[i]
            j, k = i+1, length-1
            while j < k:
                currSum = nums[j] + nums[k]
                if currSum == neededSum:
                    ans.add((nums[i], nums[j], nums[k]))
                    j += 1
                    k -= 1
                elif currSum > neededSum: k -= 1
                else: j += 1
        return list(ans)
"""
# solution uses O(n^2) space for ans in addition to return O(n^2) space, since we are not returning ans
#    -> never use set() to get rid of duplicates

"""
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans = []
        length, checkedI = len(nums), set()
        nums.sort()
        for i in range(length):
            if nums[i] in checkedI: continue
            checkedI.add(nums[i])
            neededSum = -nums[i]
            j, k = i+1, length-1
            checkedJ = set()
            while j < k:
                if nums[j] in checkedJ: 
                    j += 1
                    continue
                currSum = nums[j] + nums[k]
                if currSum == neededSum:
                    ans.append((nums[i], nums[j], nums[k]))
                    checkedJ.add(nums[j])
                    j += 1
                    k -= 1
                elif currSum > neededSum: k -= 1
                else: j += 1
        return ans
"""
# using checkedI takes n memory, can just compare number to previous number (since everything is sorted)

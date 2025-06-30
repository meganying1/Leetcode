# https://leetcode.com/problems/number-of-subsequences-that-satisfy-the-given-sum-condition
# topics: array, two pointers, binary search, sorting
# difficulty: medium

# problem:
# You are given an array of integers nums and an integer target.
# Return the number of non-empty subsequences of nums such that the sum of the minimum and maximum element on it is less or equal to target. Since the answer may be too large, return it modulo 109 + 7.

class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        modulo = 10 ** 9 + 7
        ans = 0
        n = len(nums)
        nums.sort()
        for i in range(n):
            minVal = nums[i]
            maxVal = target - minVal
            if maxVal < minVal: break
            j = bisect_right(nums, target-minVal)
            if j == n or nums[j] > maxVal: j -= 1
            ans += (2 ** (j-i)) % modulo
        return ans % modulo
# time complexity: O(nlogn)
#   sorting takes O(nlogn) time
#   outer for loop has n iterations and in each iteration, we conduct binary search, which takes O(logn) time
# space complexity: O(sort)

# approach:
#   sort array so that we can use binary search
#   consider each element of the array as the minimum value in the subsequence, and determine the index of the corresponding maximum value such that (max + min <= target)
#   calculate the number of subsequences between those two indices
# why sorting is ok even though we are looking for subsequences:
#   since we are only looking at the minimum and maximum of each subsequence, it doesn't matter the order elements within the subsequence
#   we can pick to include whatever elements we want within the subsequences as long as they don't exceed the minimum / maximum values

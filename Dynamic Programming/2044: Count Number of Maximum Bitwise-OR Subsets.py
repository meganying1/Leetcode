# https://leetcode.com/problems/count-number-of-maximum-bitwise-or-subsets/
# topics: array, backtracking, bit manipulation, enumeration
# difficulty: medium

# problem:
# Given an integer array nums, find the maximum possible bitwise OR of a subset of nums and return the number of different non-empty subsets with the maximum bitwise OR.
# An array a is a subset of an array b if a can be obtained from b by deleting some (possibly zero) elements of b. Two subsets are considered different if the indices of the elements chosen are different.
# The bitwise OR of an array a is equal to a[0] OR a[1] OR ... OR a[a.length - 1] (0-indexed).

# bottom-up dynamic programming solution
class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        dp = [0] * (1 << 17)
        dp[0] = 1
        currMax = 0
        for n in nums:
            for i in range(currMax, -1, -1):
                dp[i|n] += dp[i]
            currMax |= n
        return dp[currMax]
# time complexity: O(n*m), where m is the max or value
# space complexity: O(2^17)

# we create a dp array of size 2^17, where dp[i] represents the number of subsets with a cumulative OR value of i
#   dp[0] = 1 because only one subset has an OR value of 0 (an empty subset)
#   the largest possible number in nums is 10^5 which requires 17 bits, thus the maximum possible OR value has 17 bits
# we iterate over nums and OR it with all the possible subset OR values, which is all values between 0 and the maximum OR value so far
#   we iterate backwards to avoid double counting

# backtracking solution
class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        ans = 0
        currMax = -float('inf')
        n = len(nums)

        def helper(i, curr):
            nonlocal ans, currMax
            if i == n:
                if curr > currMax:
                    currMax = curr
                    ans = 1
                elif curr == currMax: ans += 1
                return
            helper(i+1, curr)
            helper(i+1, curr | nums[i])
        
        helper(0, 0)
        return ans
# time complexity: O(2^n)
#   the size of the tree is 2^n
#       the depth of the tree is n and the branching factor is 2
# space complexity: O(n)

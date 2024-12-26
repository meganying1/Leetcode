# https://leetcode.com/problems/target-sum/
# difficulty: medium
# topics: array, dynamic programming, backtracking

# problem:
# You are given an integer array nums and an integer target.
# You want to build an expression out of nums by adding one of the symbols '+' and '-' before each integer in nums and then concatenate all the integers.
# For example, if nums = [2, 1], you can add a '+' before 2 and a '-' before 1 and concatenate them to build the expression "+2-1".
# Return the number of different expressions that you can build, which evaluates to target.

# top-down dynamic programming with memoization
class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        cache = {}
        
        def dp(i, neededSum):
            if i == 0:
                ans = 0
                if neededSum == nums[i]: ans += 1
                if neededSum == -nums[i]: ans += 1 
                return ans
            if (i, neededSum) in cache: return cache[(i, neededSum)]
            ans = dp(i-1, neededSum - nums[i]) + dp(i-1, neededSum + nums[i])
            cache[(i, neededSum)] = ans
            return ans

        return dp(len(nums)-1, target)
# time complexity: O(n*k), where k is target sum
# space complexity: O(n*k)

# backtracking (time limit exceeded)
class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        n = len(nums)
        ans = 0
        
        def backtrack(i, currSum):
            nonlocal ans
            if i == n:
                if currSum == target: ans += 1
                return
            backtrack(i+1, currSum - nums[i])
            backtrack(i+1, currSum + nums[i])

        backtrack(0, 0)
        return ans
# time complexity: O(2^n)
#   at each level in recursion stack, we have 2 choices
#   our recursion stack has a depth of n
# space complexity: O(n)

# https://leetcode.com/problems/combination-sum/description/
# difficulty: medium
# topics: array, backtracking

# problem:
# Given an array of distinct integers candidates and a target integer target, return a list of all unique combinations of candidates where the chosen numbers sum to target. You may return the combinations in any order.
# The same number may be chosen from candidates an unlimited number of times. Two combinations are unique if the frequency of at least one of the chosen numbers is different.
# The test cases are generated such that the number of unique combinations that sum up to target is less than 150 combinations for the given input.

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        length = len(candidates)
        ans = []
        path = []
        
        def backtrack(i, needed):
            if i == length: return
            if needed == 0:
                ans.append(path[:])
                return
            if candidates[i] > needed: return
            backtrack(i+1, needed)
            path.append(candidates[i])
            backtrack(i, needed-candidates[i])
            path.pop()
        
        backtrack(0, target)
        return ans

"""
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        length = len(candidates)
        ans = []
        path = []
        
        def backtrack(i, needed):
            if i == length: return
            if needed == 0:
                ans.append(path[:])
                return
            for j in range(i, length):
                if candidates[j] > needed: break
                path.append(candidates[j])
                backtrack(j, needed-candidates[j])
                path.pop()
        
        backtrack(0, target)
        return ans
  """
# don't need for loop in backtrack function

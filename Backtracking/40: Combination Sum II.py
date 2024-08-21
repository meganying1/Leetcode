# https://leetcode.com/problems/combination-sum-ii/
# difficulty: medium
# topics: array, backtracking

# problem:
# Given a collection of candidate numbers (candidates) and a target number (target), find all unique combinations in candidates where the candidate numbers sum to target.
# Each number in candidates may only be used once in the combination.
# Note: The solution set must not contain duplicate combinations.

"""
class Solution(object):
    def combinationSum2(self, candidates, target):
        candidates.sort()
        n = len(candidates)
        path = []
        ans = []
        
        def backtrack(i, totalSum):
            if totalSum == target:
                ans.append(path[:])
                return
            if totalSum > target or i == n: return
            j = i+1
            while j < n:
                if candidates[j] != candidates[i]: break
                j += 1
            backtrack(j, totalSum)
            path.append(candidates[i])
            backtrack(i+1, totalSum+candidates[i])
            path.pop()
        
        backtrack(0, 0)
        return ans
"""
# time complexity: O(n * 2^n)
    # size of tree: 2^n
        # branching factor is 2 and depth of tree is n
    # time complexity of each node: O(n)
# space complexity: O(sort + n)
    # minimum amount of space needed is O(max(sort, n))
        # we can reusue space from sort for target, but only if it is garbage collected quickly enough

# https://leetcode.com/problems/combination-sum-iii
# difficulty: medium
# topics: array, backtracking

# problem:
# Find all valid combinations of k numbers that sum up to n such that the following conditions are true:
#   Only numbers 1 through 9 are used.
#   Each number is used at most once.
# Return a list of all possible valid combinations. The list must not contain the same combination twice, and the combinations may be returned in any order.

class Solution(object):
    def combinationSum3(self, k, n):
        path = []
        ans = []
        
        def backtrack(num, totalCount, totalSum):
            if totalCount == k and totalSum == n:
                ans.append(path[:])
                return
            if num > 9 or totalCount > k or totalSum > n: return
            backtrack(num+1, totalCount, totalSum)
            path.append(num)
            backtrack(num+1, totalCount+1, totalSum+num)
            path.pop()
        
        backtrack(1, 0, 0)
        return ans
# time complexity: O(k * 9^k)
  # size of tree is 9^k
    # branching factor is 9
      # each number 1 through 9 is considered once in the context of a particular combination, and there are 9 choices at first call, 8 at second, 7 at third, etc.
    # max depth of tree is k
  # time complexity of each node: O(k)
# space complexity: O(k)
  # callstack has max depth of k
  # path uses k space

"""
class Solution(object):
    def combinationSum3(self, k, n):
        path = []
        ans = []
        used = [False] * 9
        
        def backtrack(num, totalCount, totalSum):
            if totalCount > k or totalSum > n: return
            if totalCount == k and totalSum == n:
                ans.append(path[:])
                return
            used[num-1] = True
            for i in range(num, 10):
                if not used[i-1]:
                    path.append(i)
                    backtrack(i, totalCount+1, totalSum+i)
                    path.pop()
            used[num-1] = False
        
        for i in range(1, 10):
            if not used[i-1]:
                path.append(i)
                backtrack(i, 1, i)
                path.pop()
        return ans
"""

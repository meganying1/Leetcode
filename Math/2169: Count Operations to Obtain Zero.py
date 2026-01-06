# https://leetcode.com/problems/count-operations-to-obtain-zero/
# difficulty: easy
# topics: math, simulation

# description:
# You are given two non-negative integers num1 and num2.
# In one operation, if num1 >= num2, you must subtract num2 from num1, otherwise subtract num1 from num2.
# For example, if num1 = 5 and num2 = 4, subtract num2 from num1, thus obtaining num1 = 1 and num2 = 4. However, if num1 = 4 and num2 = 5, after one operation, num1 = 4 and num2 = 1.
# Return the number of operations required to make either num1 = 0 or num2 = 0.

class Solution:
    def countOperations(self, num1: int, num2: int) -> int:
        ans = 0
        while num1 and num2:
            if num1 < num2: num1, num2 = num2, num1
            ans += num1 // num2
            num1 %= num2
        return ans
# time complexity: O(log(min(num1, num2))
#   each iteration reduces at least one of the numbers by at least half and number of iterations is bounded by how many times we can keep dividing down the smaller number
# space complexity: O(1)

"""
class Solution:
    def countOperations(self, num1: int, num2: int) -> int:
        ans = 0
        while num1 and num2:
            if num1 > num2: num1 -= num2
            else: num2 -= num1
            ans += 1
        return ans
"""
# time complexity: O(max(num1, num2))
#   in the worst case scenario, we have 1 as one of our numbers
# space complexity: O(1)

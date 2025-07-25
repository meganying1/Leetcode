# https://leetcode.com/problems/max-difference-you-can-get-from-changing-an-integer/
# difficulty: medium
# topics: math, greedy

# problem:
# You are given an integer num. You will apply the following steps to num two separate times:
#   Pick a digit x (0 <= x <= 9).
#   Pick another digit y (0 <= y <= 9). Note y can be equal to x.
#   Replace all the occurrences of x in the decimal representation of num by y.
# Let a and b be the two results from applying the operation to num independently.
# Return the max difference between a and b.
# Note that neither a nor b may have any leading zeros, and must not be 0.

class Solution:
    def maxDiff(self, num: int) -> int:
        maxVal = minVal = str(num)
        for digit in maxVal:
            if digit != '9':
                maxVal = maxVal.replace(digit, '9')
                break
        for i in range(len(minVal)):
            digit = minVal[i]
            if i == 0:
                if digit != '1':
                    minVal = minVal.replace(digit, '1')
                    break
            else:
                if digit != '0' and minVal[0] != digit:
                    minVal = minVal.replace(digit, '0')
                    break
        return int(maxVal) - int(minVal)
# time complexity: O(n), where n is the number of digits in num
# space complexity: O(n)

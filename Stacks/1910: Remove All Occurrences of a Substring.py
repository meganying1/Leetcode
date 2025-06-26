# https://leetcode.com/problems/remove-all-occurrences-of-a-substring/
# topics: string, stack, simulation
# difficulty: medium

# problem:
# Given two strings s and part, perform the following operation on s until all occurrences of the substring part are removed:
#   Find the leftmost occurrence of the substring part and remove it from s.
# Return s after removing all occurrences of part.
# A substring is a contiguous sequence of characters in a string.

class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        stack = []
        m = len(part)
        for c in s:
            stack.append(c)
            if len(stack) >= m and "".join(stack[-m:]) == part:
                for i in range(m): stack.pop()
        return "".join(stack)
# time complexity: O(n*m), where n is len(s) and m is len(part)
#   the outer loop has n steps
#   checking and removing the top m characters of the stack takes O(m) time
# space complexity: O(n+m)

"""
class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        stack1, stack2 = [], []
        m = len(part)
        for c in s:
            stack1.append(c)
            i = m-1
            while stack1 and i >= 0 and stack1[-1] == part[i]:
                stack2.append(stack1.pop())
                i -= 1
            if i != -1:
                while stack2:
                    stack1.append(stack2.pop())
            else: stack2 = []
        return "".join(stack1)
"""
# time complexity: O(n*m), where n is len(s) and m is len(part)
#   the outer loop has n steps
#     during each step, we may traverse over all characters of part up to 2 times
# space complexity: O(n+m)
#   we store up to n characters in stack1 and up to m characters in stack2

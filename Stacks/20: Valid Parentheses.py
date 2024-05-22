# https://leetcode.com/problems/valid-parentheses/
# difficulty: easy
# topics: string, stack

# problem:
# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
# An input string is valid if:
#   Open brackets must be closed by the same type of brackets.
#   Open brackets must be closed in the correct order.
#   Every close bracket has a corresponding open bracket of the same type.

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for c in s:
            if c in ("(", "{", "["):
                stack.append(c)
            else:
                if not stack: return False
                last = stack.pop()
                if ((c == ")" and last != "(") or (c == "}" and last != "{") or 
                (c == "]" and last != "[")): return False
        return not stack
# time complexity: O(n)
# space complexity: O(n)

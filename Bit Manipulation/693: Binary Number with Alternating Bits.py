# https://leetcode.com/problems/binary-number-with-alternating-bits/
# difficulty: easy
# topics: bit manipulation

class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        prev = n & 1
        n >>= 1
        while n > 0:
            curr = n & 1
            if prev ^ curr == 0: return False
            n >>= 1
            prev = curr
        return True
# time complexity: O(logn)
# space complexity: O(1)

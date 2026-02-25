# https://leetcode.com/problems/sort-integers-by-the-number-of-1-bits/
# difficulty: easy
# topics: array, bit manipulation, sorting, counting

class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        
        def countOnes(n):
            ans = 0
            while n:
                if n & 1 == 1: ans += 1
                n >>= 1
            return ans

        arr.sort(key=lambda x: (countOnes(x), x))
        return arr
# time complexity: O(nlogn)
#   it takes O(b) time to find number of ones, where b is number of bits
#   since b is at most 32, we can consider this O(1)
#   sort takes O(nlogn) time
# space complexity: O(n)

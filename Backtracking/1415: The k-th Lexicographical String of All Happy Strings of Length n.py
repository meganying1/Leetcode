# https://leetcode.com/problems/the-k-th-lexicographical-string-of-all-happy-strings-of-length-n/
# difficulty: medium
# topics: string, backtracking

# description:
# A happy string is a string that:
#   consists only of letters of the set ['a', 'b', 'c'].
#   s[i] != s[i + 1] for all values of i from 1 to s.length - 1 (string is 1-indexed).
# For example, strings "abc", "ac", "b" and "abcbabcbcb" are all happy strings and strings "aa", "baa" and "ababbc" are not happy strings.
# Given two integers n and k, consider a list of all happy strings of length n sorted in lexicographical order.
# Return the kth string of this list or return an empty string if there are less than k happy strings of length n.

class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        ans = ''
        path = []
        count = 0
        
        def backtrack():
            nonlocal count, ans
            if ans != '': return
            if len(path) == n:
                count += 1
                if count == k:
                    ans = ''.join(path)
                return
            for l in 'abc':
                if path and path[-1] == l: continue
                path.append(l)
                backtrack()
                path.pop()
        
        backtrack()
        return ans
# time complexity: O(2^n)
#   branching factor is 2 because we only call backtrack with the two letters
#   depth of recursion tree is n
# space complexity: O(n)
#   memory for recursion stack is n
#   memory for path is n

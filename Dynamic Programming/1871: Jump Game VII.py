# https://leetcode.com/problems/jump-game-vii/
# difficulty: medium
# topics: string, dynamic programming, prefix sum, sliding window

# description:
# You are given a 0-indexed binary string s and two integers minJump and maxJump. In the beginning, you are standing at index 0, which is equal to '0'. You can move from index i to index j if the following conditions are fulfilled:
#   i + minJump <= j <= min(i + maxJump, s.length - 1), and
#   s[j] == '0'.
# Return true if you can reach index s.length - 1 in s, or false otherwise.

class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        n = len(s)
        if s[-1] == '1': return False
        dp = [False] * n
        dp[0] = True
        reachable = 0
        for i in range(minJump, n):
            if dp[i - minJump]: reachable += 1
            if i - maxJump - 1 >= 0 and dp[i - maxJump - 1]: reachable -= 1
            if reachable > 0 and s[i] == '0': dp[i] = True
        return dp[n-1]
# time complexity: O(n)
# space complexity: O(n)

# For every index i, a previous index j can jump to i if (j + minJump) <= i <= (j + maxJump)
# Therefore, all valid previous jump positions for index i lie inside [i - maxJump , i - minJump]
# Index i is reachable if s[i] == '0' and an index inside [i - maxJump , i - minJump] is reachable
# Solution:
#    maintain a sliding window of possible previous jump positions and count the number of reachable indices
#    dp[i] tells us if index i is reachable
#    as we slide the window over, we:
#        add 1 to reachable indices if s[i - minJump] is reachable, since it enters the window
#        subtract 1 to reachable indices if s[i - maxJump - 1] is reachable, since it leaves the window

# https://leetcode.com/problems/taking-maximum-energy-from-the-mystic-dungeon
# difficulty: medium
# topics: array, prefix sum

# description:
# In a mystic dungeon, n magicians are standing in a line. Each magician has an attribute that gives you energy. Some magicians can give you negative energy, which means taking energy from you.
# You have been cursed in such a way that after absorbing energy from magician i, you will be instantly transported to magician (i + k). This process will be repeated until you reach the magician where (i + k) does not exist.
# In other words, you will choose a starting point and then teleport with k jumps until you reach the end of the magicians' sequence, absorbing all the energy during the journey.
# You are given an array energy and an integer k. Return the maximum possible energy you can gain.
# Note that when you are reach a magician, you must take energy from them, whether it is negative or positive energy.

class Solution:
    def maximumEnergy(self, energy: List[int], k: int) -> int:
        n = len(energy)
        dp = [0] * n
        for i in range(n):
            if i < k: dp[n-i-1] = energy[n-i-1]
            else: dp[n-i-1] = dp[n-i-1+k] + energy[n-i-1]
        return max(dp)
# idea: dp[i] is the amount of energy you gain by starting at index i
# time complexity: O(n)
# space complexity: O(n)

"""
class Solution:
    def maximumEnergy(self, energy: List[int], k: int) -> int:
        n, ans = len(energy), -float('inf')
        for i in range(n):
            currSum = energy[i]
            for j in range(i+k, n, k):
                currSum += energy[j]
            ans = max(ans, currSum)
        return ans
"""
# time complexity: O(n^2)
# space complexity: O(1)

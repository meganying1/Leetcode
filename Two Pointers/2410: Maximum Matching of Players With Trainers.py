# https://leetcode.com/problems/maximum-matching-of-players-with-trainers/
# topics: array, greedy, two pointers, sorting
# difficulty: medium

# probem:
# You are given a 0-indexed integer array players, where players[i] represents the ability of the ith player. You are also given a 0-indexed integer array trainers, where trainers[j] represents the training capacity of the jth trainer.
# The ith player can match with the jth trainer if the player's ability is less than or equal to the trainer's training capacity. Additionally, the ith player can be matched with at most one trainer, and the jth trainer can be matched with at most one player.
# Return the maximum number of matchings between players and trainers that satisfy these conditions.

class Solution:
    def matchPlayersAndTrainers(self, players: List[int], trainers: List[int]) -> int:
        ans = 0
        players.sort()
        trainers.sort()
        i, j = 0, 0
        n, m = len(players), len(trainers)
        while i < n and j < m:
            if players[i] <= trainers[j]:
                i += 1
                ans += 1
            j += 1
        return ans
# time complexity: O(nlogn + mlogm), where n is len(players) and m is len(trainers)
# space complexity: O(sort)

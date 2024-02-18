# https://leetcode.com/problems/successful-pairs-of-spells-and-potions/description/
# difficulty: medium
# topics: array, two pointers, binary search, sorting

# problem:
# You are given two positive integer arrays spells and potions, of length n and m respectively, where spells[i] represents the strength of the ith spell and potions[j] represents the strength of the jth potion.
# You are also given an integer success. A spell and potion pair is considered successful if the product of their strengths is at least success.
# Return an integer array pairs of length n where pairs[i] is the number of potions that will form a successful pair with the ith spell.

class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        numPotions = len(potions)
        ans = []
        potions.sort()
        for spell in spells:
            needed = math.ceil(success / spell)
            ans.append(numPotions - bisect_left(potions, needed))
        return ans

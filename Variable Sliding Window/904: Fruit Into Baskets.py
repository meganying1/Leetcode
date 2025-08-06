# https://leetcode.com/problems/fruit-into-baskets/
# topics: array, hash table, sliding window
# difficulty: medium

# problem:
# You are visiting a farm that has a single row of fruit trees arranged from left to right. The trees are represented by an integer array fruits where fruits[i] is the type of fruit the ith tree produces.
# You want to collect as much fruit as possible. However, the owner has some strict rules that you must follow:
#   You only have two baskets, and each basket can only hold a single type of fruit. There is no limit on the amount of fruit each basket can hold.
#   Starting from any tree of your choice, you must pick exactly one fruit from every tree (including the start tree) while moving to the right. The picked fruits must fit in one of your baskets.
#   Once you reach a tree with fruit that cannot fit in your baskets, you must stop.
# Given the integer array fruits, return the maximum number of fruits you can pick.

class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        n = len(fruits)
        l = r = ans = 0
        counts = defaultdict(int)
        while r < n:
            counts[fruits[r]] += 1
            r += 1
            while len(counts) > 2:
                counts[fruits[l]] -= 1
                if counts[fruits[l]] == 0:
                    del counts[fruits[l]]
                l += 1
            ans = max(ans, r-l)
        return ans
# time complexity: O(n)
# space complexity: O(1)

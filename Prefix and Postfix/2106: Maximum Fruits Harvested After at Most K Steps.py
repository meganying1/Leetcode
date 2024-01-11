# https://leetcode.com/problems/maximum-fruits-harvested-after-at-most-k-steps/description/
# difficulty: hard
# topics: array, binary search, sliding window, prefix sum

# problem:
# Fruits are available at some positions on an infinite x-axis. You are given a 2D integer array fruits where fruits[i] = [positioni, amounti] depicts amounti fruits at the position positioni. fruits is already sorted by positioni in ascending order, and each positioni is unique.
# You are also given an integer startPos and an integer k. Initially, you are at the position startPos. From any position, you can either walk to the left or right. It takes one step to move one unit on the x-axis, and you can walk at most k steps in total. For every position you reach, you harvest all the fruits at that position, and the fruits will disappear from that position.
# Return the maximum total number of fruits you can harvest.

from bisect import bisect_left

class Solution:
    def maxTotalFruits(self, fruits: List[List[int]], startPos: int, k: int) -> int:
        fruitList = [pos for [pos, num] in fruits]
        length = len(fruitList)

        # if k is 0, max fruits is number of fruits at start position
        if k == 0:
            ind = bisect_left(fruitList, startPos)
            if ind >= length or startPos != fruits[ind][0]: return 0
            return fruits[ind][1]

        prefix = [[pos, num] for [pos, num] in fruits]
        for i in range(1, length): prefix[i][1] += prefix[i-1][1]
        fruitList.insert(0, -1)
        prefix.insert(0, [-1, 0])

        def getFruits(sumFruits, left, right, fruitList):
            leftInd, rightInd = bisect_left(fruitList, left)-1, bisect_left(fruitList, right)
            if rightInd >= len(fruitList) or fruitList[rightInd] != right: rightInd -= 1
            if leftInd < 0: return sumFruits[rightInd][1]
            else: return sumFruits[rightInd][1] - sumFruits[leftInd][1]

        maxFruits = 0
        # try going left and turning right
        for left in range(max(0, startPos-k), startPos+1):
            if startPos-left > 2 * k: right = startPos
            else: right = startPos + (k - (2 * (startPos-left)))
            maxFruits = max(maxFruits, getFruits(prefix, left, right, fruitList))
            
        # try going right and turning left
        for right in range(min(fruits[-1][0], startPos), min(fruits[-1][0]+1, startPos+k+1)):
            if right-startPos > 2 * k: left = startPos 
            elif right < startPos: left = startPos-k
            else: left = startPos - (k - (2 * (right-startPos)))
            maxFruits = max(maxFruits, getFruits(prefix, left, right, fruitList))
        
        return maxFruits
        

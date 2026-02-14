# https://leetcode.com/problems/champagne-tower/
# difficulty: medium
# topics: dynamic programming

# description:
# We stack glasses in a pyramid, where the first row has 1 glass, the second row has 2 glasses, and so on until the 100th row.  Each glass holds one cup of champagne.
# Then, some champagne is poured into the first glass at the top.  When the topmost glass is full, any excess liquid poured will fall equally to the glass immediately to the left and right of it.  When those glasses become full, any excess champagne will fall equally to the left and right of those glasses, and so on.  (A glass at the bottom row has its excess champagne fall on the floor.)
# For example, after one cup of champagne is poured, the top most glass is full.  After two cups of champagne are poured, the two glasses on the second row are half full.  After three cups of champagne are poured, those two cups become full - there are 3 full glasses total now.  After four cups of champagne are poured, the third row has the middle glass half full, and the two outside glasses are a quarter full, as pictured below.

class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        if poured == 0: return 0
        dp = [[0] * (i+1) for i in range(query_row + 2)]
        dp[0][0] = poured
        for row in range(query_row + 1):
            for glass in range(row + 1):
                if dp[row][glass] > 1:
                    excess = (dp[row][glass] - 1) / 2
                    dp[row][glass] = 1
                    dp[row + 1][glass] += excess
                    dp[row + 1][glass + 1] += excess
        return dp[query_row][query_glass]
# idea:
# a glass can fit one cup, and if we pour more than one cup into it, the excess is split equally between the left and right cup underneath it
# for each cup in each row, we calculate the overflow and distribute it to the cups below it
      
# time complexity: O(r^2), where r = query_row
# space complexity: O(r^2)

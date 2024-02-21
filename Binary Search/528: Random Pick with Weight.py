# https://leetcode.com/problems/random-pick-with-weight/description/
# difficulty: medium
# topics: array, math, binary search, prefix sum, randomization

# problem:
# You are given a 0-indexed array of positive integers w where w[i] describes the weight of the ith index.
# You need to implement the function pickIndex(), which randomly picks an index in the range [0, w.length - 1] (inclusive) and returns it. The probability of picking an index i is w[i] / sum(w).
#   For example, if w = [1, 3], the probability of picking index 0 is 1 / (1 + 3) = 0.25 (i.e., 25%), and the probability of picking index 1 is 3 / (1 + 3) = 0.75 (i.e., 75%).

class Solution:

    def __init__(self, w: List[int]):
        self.prefix = [num for num in w]
        self.length = len(w)
        for i in range(1, self.length): self.prefix[i] += self.prefix[i-1]

    def pickIndex(self) -> int:
        num = random.randint(1, self.prefix[-1])
        lo, hi = 0, self.length-1
        while lo <= hi:
            mid = lo + ((hi-lo)//2)
            if self.prefix[mid] < num: lo = mid+1
            else: hi = mid-1
        return lo

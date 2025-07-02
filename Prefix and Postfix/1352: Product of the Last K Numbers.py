# https://leetcode.com/problems/product-of-the-last-k-numbers/
# topics: array, math, design, data stream, prefix sum
# difficulty: medium

# problem:
# Design an algorithm that accepts a stream of integers and retrieves the product of the last k integers of the stream.
# Implement the ProductOfNumbers class:
#   ProductOfNumbers() Initializes the object with an empty stream.
#   void add(int num) Appends the integer num to the stream.
#   int getProduct(int k) Returns the product of the last k numbers in the current list. You can assume that always the current list has at least k numbers.
# The test cases are generated so that, at any time, the product of any contiguous sequence of numbers will fit into a single 32-bit integer without overflowing.

class ProductOfNumbers:

    def __init__(self):
        self.stream = [1]
        self.length = 1

    def add(self, num: int) -> None:
        if not self.stream:
            self.stream.append(num)
            self.length += 1
        elif num:
            self.stream.append(num * self.stream[-1])
            self.length += 1
        else:
            self.stream = [1]
            self.length = 1

    def getProduct(self, k: int) -> int:
        if self.length < k+1: return 0
        else: return self.stream[-1] // self.stream[-k-1]

# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)

# time complexity of add(self, num) and getProduct(self, k): O(1)

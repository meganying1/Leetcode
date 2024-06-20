# https://leetcode.com/problems/sum-of-two-integers/
# difficulty: medium
# topics: math, bit manipulation

# problem:
# Given two integers a and b, return the sum of the two integers without using the operators + and -.

class Solution:
    def getSum(self, a: int, b: int) -> int:
        mask = 0xFFFFFFFF
        while b & mask > 0:
            carryOver = (a & b) << 1
            a = a ^ b
            b = carryOver
        return a & mask if b > 0 else a

# time complexity: O(1)
# space complexity: O(1)
      
# logic:
#     & operator shows us positions that need a carry, and carry gets applied one bit to the left of where it was discovered
#     ^ operator is used to perform the addition
#     << operator is used to turn carry into what will apply in next iteration
#     a holds running addition result and b holds carries
# python allows for unlimited length of integers, so carry will never go to zero, leading to an infinite loop
#     we bound the length of the carry using a mask, allowing us to keep only the last 32 bits
#     eventually carry will become 0 when it exceeds 32 bits
# we now successfully get out of the while loop, but a also only has 32 bits
# if a is negative, we need to convert it to two's complement: flip all bits and add one
#     we cannot use ~ operator because it will flip infinite bits, not just the last 32 bits
#     instead, we use ^ operator with OxFFFFFFFF because xoring bits with 1 has the same effect as flipping the bits
# in the final check:
#     if b == 0, that means there is no carry
#     when there is a negative number, the carry bit will continue until it exceeds 32 bit mask, so we use a bit mask on a

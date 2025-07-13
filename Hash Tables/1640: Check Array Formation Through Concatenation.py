# https://leetcode.com/problems/check-array-formation-through-concatenation/
# topics: array, hash table
# difficulty: easy

# problem:
# You are given an array of distinct integers arr and an array of integer arrays pieces, where the integers in pieces are distinct. Your goal is to form arr by concatenating the arrays in pieces in any order. However, you are not allowed to reorder the integers in each array pieces[i].
# Return true if it is possible to form the array arr from pieces. Otherwise, return false.

class Solution:
    def canFormArray(self, arr: List[int], pieces: List[List[int]]) -> bool:
        piecesIndices = {p[0]:p for p in pieces}
        i = 0
        while i < len(arr):
            if arr[i] not in piecesIndices: return False
            possiblePiece = piecesIndices[arr[i]]
            for val in possiblePiece:
                if arr[i] != val: return False
                i += 1
        return True
# time complexity: O(n), where n is is len(arr)
# space complexity: O(p), where p is len(pieces)

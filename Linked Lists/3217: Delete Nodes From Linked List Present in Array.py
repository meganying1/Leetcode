# https://leetcode.com/problems/find-resultant-array-after-removing-anagrams/
# difficulty: medium
# topics: array, hash table, linked list

# description:
# You are given an array of integers nums and the head of a linked list. Return the head of the modified linked list after removing all nodes from the linked list that have a value that exists in nums.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:
        numsSet = set(nums)
        dummy = curr = ListNode(None)
        while head:
            if head.val not in numsSet:
                curr.next = head
                curr = curr.next
            head = head.next
        curr.next = None
        return dummy.next
# time complexity: O(n + m), where n is len(nums) and m is len(head)
# space complexity: O(n)

# https://leetcode.com/problems/linked-list-cycle/description/
# difficulty: easy
# topics: hash table, linked list, two pointers

# problem:
# Given head, the head of a linked list, determine if the linked list has a cycle in it.
# There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer. Internally, pos is used to denote the index of the node that tail's next pointer is connected to. Note that pos is not passed as a parameter.
# Return true if there is a cycle in the linked list. Otherwise, return false.

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        tortoise = hare = head
        while hare and hare.next:
            tortoise = tortoise.next
            hare = hare.next.next
            if tortoise == hare: return True
        return False
# time complexity: O(n)
# space complexity: O(1)

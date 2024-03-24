# https://leetcode.com/problems/reverse-nodes-in-k-group/description/
# difficulty: hard
# topics: linked list, recursion

# problem:
# Given the head of a linked list, reverse the nodes of the list k at a time, and return the modified list.
# k is a positive integer and is less than or equal to the length of the linked list. If the number of nodes is not a multiple of k then left-out nodes, in the end, should remain as it is.
# You may not alter the values in the list's nodes, only nodes themselves may be changed.

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        
        def reverse(head):
            prev, curr = None, head
            while curr:
                nextNode = curr.next
                curr.next = prev
                prev = curr
                curr = nextNode
            return prev
        
        start = end = head
        dummy = prev = ListNode()
        while end:
            for i in range(k-1):
                end = end.next
                if not end: break
            if not end:
                prev.next = rest
                break
            rest = end.next
            end.next = None
            prev.next = reverse(start)
            while prev.next: prev = prev.next
            start = end = rest
        return dummy.next
  # time complexity: O(n)
  # space complelxity: O(1)

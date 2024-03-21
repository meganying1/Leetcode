# https://leetcode.com/problems/remove-nth-node-from-end-of-list/description/
# difficulty: medium
# topics: linked list, two pointers

# problem:
# Given the head of a linked list, remove the nth node from the end of the list and return its head.

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head.next: return None
        endPtr = head
        for i in range(n): endPtr = endPtr.next
        if not endPtr: return head.next
        removePtr = head
        while endPtr and endPtr.next:
            endPtr = endPtr.next
            removePtr = removePtr.next
        removePtr.next = removePtr.next.next
        return head
# time complexity: O(n)
# space complexity: O(1)

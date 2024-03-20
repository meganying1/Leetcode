# https://leetcode.com/problems/reverse-linked-list/
# difficulty: easy
# topics: linked list, recursion

# Given the head of a singly linked list, reverse the list, and return the reversed list.

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr, prev = head, None
        while curr:
            nextNode = curr.next
            curr.next = prev
            prev = curr
            curr = nextNode
        return prev 
# iterative solution
# time complexity: O(n)
# space complexity: O(1)

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        def reverse(prev, curr):
            if curr == None: return prev
            nextNode = curr.next
            curr.next = prev
            return reverse(curr, nextNode)

        return reverse(None, head)
# recursive solution
# time complexity: O(n)
# space complexity: O(n)
#     recursion never has a space complexity of O(1)
#     space complexity is proportional to depth of recursion tree

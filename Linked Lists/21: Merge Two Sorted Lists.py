# https://leetcode.com/problems/merge-two-sorted-lists/description/
# difficulty: easy
# topics: linked list, recursion

# problem:
# You are given the heads of two sorted linked lists list1 and list2.
# Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.
# Return the head of the merged linked list.

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 == None: return list2
        if list2 == None: return list1
        curr1, curr2 = list1, list2
        head = curr = ListNode()
        while curr1 and curr2:
            if curr1.val < curr2.val:
                curr.next = curr1
                curr1 = curr1.next
            else:
                curr.next = curr2
                curr2 = curr2.next
            curr = curr.next
        if curr1: curr.next = curr1
        else: curr.next = curr2
        return head.next
# iterative solution
# time complexity: O(min(n,m))
# space complexity: O(1)

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
      if list1 == None: return list2
      if list2 == None: return list1
      if list1.val < list2.val: 
          list1.next = self.mergeTwoLists(list1.next, list2)
          return list1
      else:
          list2.next = self.mergeTwoLists(list1, list2.next)
          return list2
# recursive solution
# time complexity: O(min(n,m))
# space complexity: O(min(n,m))

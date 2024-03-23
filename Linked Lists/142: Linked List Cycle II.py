# https://leetcode.com/problems/linked-list-cycle-ii/description/
# difficulty: medium
# topics: hash table, linked list, two pointers

# problem:
# Given the head of a linked list, return the node where the cycle begins. If there is no cycle, return null.
# There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer. Internally, pos is used to denote the index of the node that tail's next pointer is connected to (0-indexed). It is -1 if there is no cycle. Note that pos is not passed as a parameter.
# Do not modify the linked list.

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        ptr1 = ptr2 = head
        while ptr2 and ptr2.next:
            ptr1 = ptr1.next
            ptr2 = ptr2.next.next
            if ptr1 == ptr2:
                break
        if not ptr2 or not ptr2.next: return None
        ptr2 = head
        while ptr1 != ptr2:
            ptr1 = ptr1.next
            ptr2 = ptr2.next
        return ptr1
# time complexity: O(n)
# space complexity: O(1)

# proof:
#     let:
#         p = distance from beginning to the head of the cycle
#         c = distance from the head of the cycle to the point where slow and fast pointer collided: the “collision point”
#         loop = length of the cycle
#     therefore, loop - c = distance from the collision point to the head of the cycle

#     we are trying to prove that p = loop - c
#     fast pointer traveled: p + n*loop + c
#     slow pointer traveled: p + c
#     fast pointer traveled 2x as much as slow pointer: 2(p + c) = p + n*loop + c
#     2p + 2c = p + n*loop + c
#     p + c = n*loop
#     p = n*loop - c

# heap (priority queue) approach
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:  
        minHeap = []
        head = curr = ListNode(None)
        for i, node in enumerate(lists):
            if node: heapq.heappush(minHeap, (node.val, i, node))
        while minHeap:
            val, i, node = heapq.heappop(minHeap)
            curr.next = node
            curr = curr.next
            if node.next: heapq.heappush(minHeap, (node.next.val, i, node.next))
        return head.next
# time complexity: O(nlogk)
#   we push all n nodes onto a heap of size k, and pop all n nodes
# space complexity: O(k)

# divide and conquer approach
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if len(lists) == 0: return None
        if len(lists) == 1: return lists[0]

        def mergeTwoLists(list1, list2):
            head = ListNode()
            ans = head
            while list1 and list2:
                if list1.val < list2.val:
                    ans.next = list1
                    list1 = list1.next
                else:
                    ans.next = list2
                    list2 = list2.next
                ans = ans.next
            if list1: ans.next = list1
            else: ans.next = list2
            return head.next
            
        mid = len(lists) // 2
        left = self.mergeKLists(lists[:mid])
        right = self.mergeKLists(lists[mid:])
        return mergeTwoLists(left, right)
# time complexity: O(nlogk)
#   divide and conquer merges logk times
#   each merge operation processes all n nodes
# space complexity: O(logk)
#   depth of recursion stack is logk

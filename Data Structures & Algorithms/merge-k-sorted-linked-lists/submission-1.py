# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import itertools

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        tie_breaker = itertools.count()
        heap = [(l.val, next(tie_breaker), l) for l in lists]
        heapq.heapify(heap)
        current = dummy_head = ListNode()
        while heap:
            next_node = heapq.heappop(heap)[2]
            current.next = next_node
            if next_node.next:
                heapq.heappush(heap, (next_node.next.val, next(tie_breaker), next_node.next))
            current = current.next
        return dummy_head.next
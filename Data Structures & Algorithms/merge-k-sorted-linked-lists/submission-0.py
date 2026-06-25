# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:   
    def merge(self, l1, l2):
        current = dummy_head = ListNode()
        while l1 and l2:
            next_node = l1 if l1.val < l2.val else l2
            if l1.val < l2.val:
                current.next = l1
                l1 = l1.next
            else:
                current.next = l2
                l2 = l2.next
            current = current.next
        
        current.next = l1 if l1 else l2
        return dummy_head.next

    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        current = lists
        while len(current) > 1:
            next_round = []
            for i in range(0, len(current), 2):
                next_round.append(self.merge(current[i], current[i+1] if i+1 < len(current) else None))
            current = next_round
        return current[0] if len(current) else None
        
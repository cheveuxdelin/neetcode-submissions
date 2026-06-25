# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def find_middle(self, head):
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow
    
    def reverse(self, head):
        previous = None
        current = head
        while current:
            nxt = current.next
            current.next = previous
            previous = current
            current = nxt
        return previous
    
    def merge(self, l1, l2):
        dummy_head = current = ListNode()
        while l1 and l2:
            current.next = l1
            l1 = l1.next
            current = current.next
            current.next = l2
            l2 = l2.next
            current = current.next
        current.next = l1 if l1 else l2
        return dummy_head.next

    def reorderList(self, head: Optional[ListNode]) -> None:
        middle_node = self.find_middle(head)
        second_half = middle_node.next
        middle_node.next = None
        new_second_half_head = self.reverse(second_half)
        self.merge(head, new_second_half_head)
        
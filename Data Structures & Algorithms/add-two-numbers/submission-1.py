# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        current = dummy_head = ListNode()
        carry_over = 0

        while l1 and l2:
            div, mod = divmod(l1.val + l2.val + carry_over, 10)
            carry_over = div
            current.next = ListNode(mod)
            current = current.next
            l1 = l1.next
            l2 = l2.next
        
        while l1:
            div, mod = divmod(l1.val + carry_over, 10)
            carry_over = div
            current.next = ListNode(mod)
            current = current.next
            l1 = l1.next
        
        while l2:
            div, mod = divmod(l2.val + carry_over, 10)
            carry_over = div
            current.next = ListNode(mod)
            current = current.next
            l2 = l2.next
        
        if carry_over:
            current.next = ListNode(carry_over)
        
        return dummy_head.next
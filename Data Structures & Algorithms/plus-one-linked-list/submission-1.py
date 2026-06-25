# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def plusOne(self, head: ListNode) -> ListNode:
        def helper(current):
            if not current.next:
                current.val = (current.val + 1) % 10
                return current.val == 0
            else:
                carry_over = bool(helper(current.next))
                result_before_mod = current.val + carry_over
                current.val = result_before_mod % 10
                return result_before_mod >= 10
        
        carry_over = helper(head)
        if carry_over:
            return ListNode(1, head)
        else:
            return head
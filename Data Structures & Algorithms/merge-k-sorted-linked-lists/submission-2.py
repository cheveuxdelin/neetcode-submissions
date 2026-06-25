# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        def merge_two_lists(list1, list2):
            dummy_head = current = ListNode()

            while list1 and list2:
                if list1.val < list2.val:
                    current.next = list1
                    list1 = list1.next
                else:
                    current.next = list2
                    list2 = list2.next
                current = current.next
            current.next = list1 if list1 else list2
            return dummy_head.next
        
        while len(lists) > 1:
            new_list = []
            for i in range(0, len(lists), 2):
                if i+1 < len(lists):
                    new_list.append(merge_two_lists(lists[i], lists[i+1]))
                else:
                    new_list.append(lists[i])
            lists = new_list
        return lists[0] if lists else None
        
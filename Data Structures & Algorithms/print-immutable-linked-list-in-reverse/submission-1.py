# """
# This is the ImmutableListNode's API interface.
# You should not implement it, or speculate about its implementation.
# """
# class ImmutableListNode:
#     def printValue(self) -> None: # print the value of this node.
#     def getNext(self) -> 'ImmutableListNode': # return the next node.

class Solution:
    def printLinkedListInReverse(self, head: 'ImmutableListNode') -> None:
        last_printed = None

        while head != last_printed:
            current = head
            while current.getNext() != last_printed:
                current = current.getNext()
            current.printValue()
            last_printed = current
            
"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        nodes_map = {}
        # create all the copies first
        current = head
        while current:
            nodes_map[current] = Node(current.val)
            current = current.next
        
        # make all the connections
        current = head
        while current:
            nodes_map[current].next = nodes_map.get(current.next, None)
            nodes_map[current].random = nodes_map.get(current.random, None)
            current = current.next

        return nodes_map.get(head, None)
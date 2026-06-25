class Node:
    def __init__(self, key=None, value=None):
        self.previous = None
        self.next = None
        self.key = key
        self.value = value

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.size = 0
        self.left = Node()
        self.right = Node()
        self.map = {}

        self.left.next = self.right
        self.right.previous = self.left
        

    def get(self, key: int) -> int:
        if key in self.map:
            value = self.remove(key)
            self.insert(key, value)
            return value
        else:
            return -1
        

    def put(self, key: int, value: int) -> None:
        if key in self.map:
            self.remove(key)

        self.insert(key, value)
        if self.size > self.capacity:
            self.remove(self.right.previous.key)

    def insert(self, key, value):
        node = Node(key, value)
        left_next = self.left.next

        left_next.previous = node
        self.left.next = node
        node.previous = self.left
        node.next = left_next
        self.size += 1
        self.map[key] = node
    
    def remove(self, key):
        node = self.map[key]
        previous = node.previous
        nxt = node.next

        previous.next = nxt
        nxt.previous = previous
        self.map.pop(key)

        self.size -= 1
        return node.value

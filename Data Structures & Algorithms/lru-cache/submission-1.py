class LRUCache:
    class Node:
        def __init__(self, key = None, value = 0, previous = None, next = None):
            self.key = key
            self.value = value
            self.previous = previous
            self.next = next

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.head = self.Node()
        self.tail = self.Node()
        self.head.next = self.tail
        self.tail.previous = self.head
        self.map = {}
        self.size = 0

    def get(self, key: int) -> int:
        if key in self.map:
            node = self.map[key]
            self.remove(node)
            self.insert(node)
            return node.value
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.map:
            self.remove(self.map[key])
        new_node = self.Node(key, value)
        self.insert(new_node)
        if self.size > self.capacity:
            last_used_node = self.head.next
            self.remove(last_used_node)
    
    def remove(self, node):
        node.next.previous = node.previous
        node.previous.next = node.next
        self.map.pop(node.key)
        self.size -= 1

    def insert(self, node):
        node.previous = self.tail.previous
        node.next = self.tail
        self.tail.previous.next = node
        self.tail.previous = node
        self.map[node.key] = node
        self.size += 1
        
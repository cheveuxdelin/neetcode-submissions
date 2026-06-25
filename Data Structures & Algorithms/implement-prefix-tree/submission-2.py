class Node:
    def __init__(self):
        self.children = {}
        self.is_word = False

class PrefixTree:

    def __init__(self):
        self.root = Node()

    def insert(self, word: str) -> None:
        current = self.root
        for c in word:
            if c not in current.children:
                current.children[c] = Node()
            current = current.children[c]
        current.is_word = True

    def search(self, word: str) -> bool:
        current = self.root
        for c in word:
            if c not in current.children:
                return False
            current = current.children[c]
        return current.is_word
        

    def startsWith(self, prefix: str) -> bool:
        current = self.root
        for c in prefix:
            if c not in current.children:
                return False
            current = current.children[c]
        return True
        
import heapq


class TrieNode:
    def __init__(self) -> None:
        self.children: dict[str, TrieNode] = {}
        self.hot_degree = 0


class HeapElement:
    def __init__(self, hot_degree: int, value: str) -> None:
        self.hot_degree = hot_degree
        self.value = value

    def __lt__(self, other: HeapElement):
        if self.hot_degree == other.hot_degree:
            return self.value > other.value
        return self.hot_degree < other.hot_degree


class Trie:
    def __init__(self, previous_sentences: list[str], times: list[int]) -> None:
        self.root = TrieNode()
        for sentence, time in zip(previous_sentences, times):
            self.insert(list(sentence), time)

    def insert(self, sentence: list[str], times: int = 0) -> TrieNode:
        current = self.root
        for c in sentence:
            if c not in current.children:
                current.children[c] = TrieNode()
            current = current.children[c]
        current.hot_degree += times
        return current

    def retrieve(self, origin_node: TrieNode, current_word: list[str]) -> list[str]:
        heap = []

        def dfs(current: TrieNode):
            if current.hot_degree > 0:
                heapq.heappush(heap, HeapElement(current.hot_degree, "".join(current_word)))
                if len(heap) > 3:
                    heapq.heappop(heap)

            for child_c, child_node in current.children.items():
                current_word.append(child_c)
                dfs(child_node)
                current_word.pop()

        dfs(origin_node)
        heap.sort(reverse=True)
        return [element.value for element in heap]


class AutocompleteSystem:

    def __init__(self, sentences: list[str], times: list[int]):
        # step 1. build the trie
        self.trie = Trie(sentences, times)
        self.current_pointer = self.trie.root
        self.current_sentence = []

    def input(self, c: str) -> list[str]:
        # if finishing
        if c == "#":
            self.trie.insert(self.current_sentence, 1)
            
            # reset
            self.current_pointer = self.trie.root
            self.current_sentence = []
            return []
        else:
            self.current_sentence.append(c)
            
            if not self.current_pointer:
                return []

            if c in self.current_pointer.children:
                self.current_pointer = self.current_pointer.children[c]
                return self.trie.retrieve(self.current_pointer, self.current_sentence.copy())
            # new word
            else:
                self.current_pointer = None
                return []
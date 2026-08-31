# Last updated: 8/31/2026, 1:59:07 PM
class Node:
    def __init__(self, count=0):
        self.count = count
        self.keys = set()
        self.prev = None
        self.next = None


class AllOne:

    def __init__(self):
        self.head = Node()
        self.tail = Node()

        self.head.next = self.tail
        self.tail.prev = self.head

        self.map = {}

    def inc(self, key: str) -> None:
        if key not in self.map:
            node = self.head.next

            if node == self.tail or node.count != 1:
                new_node = Node(1)
                self._insert_after(self.head, new_node)
                node = new_node

            node.keys.add(key)
            self.map[key] = node

        else:
            node = self.map[key]
            next_node = node.next

            if next_node == self.tail or next_node.count != node.count + 1:
                new_node = Node(node.count + 1)
                self._insert_after(node, new_node)
                next_node = new_node

            next_node.keys.add(key)
            self.map[key] = next_node

            node.keys.remove(key)

            if len(node.keys) == 0:
                self._remove(node)

    def dec(self, key: str) -> None:
        node = self.map[key]

        if node.count == 1:
            del self.map[key]
            node.keys.remove(key)

            if len(node.keys) == 0:
                self._remove(node)

        else:
            prev_node = node.prev

            if prev_node == self.head or prev_node.count != node.count - 1:
                new_node = Node(node.count - 1)
                self._insert_after(prev_node, new_node)
                prev_node = new_node

            prev_node.keys.add(key)
            self.map[key] = prev_node

            node.keys.remove(key)

            if len(node.keys) == 0:
                self._remove(node)

    def getMaxKey(self) -> str:
        if self.tail.prev == self.head:
            return ""

        return next(iter(self.tail.prev.keys))

    def getMinKey(self) -> str:
        if self.head.next == self.tail:
            return ""

        return next(iter(self.head.next.keys))

    def _insert_after(self, node, new_node):
        new_node.prev = node
        new_node.next = node.next

        node.next.prev = new_node
        node.next = new_node

    def _remove(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev
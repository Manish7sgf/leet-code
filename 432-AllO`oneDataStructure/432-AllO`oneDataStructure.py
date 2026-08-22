# Last updated: 8/22/2026, 10:13:41 AM
1class Node:
2    def __init__(self, count=0):
3        self.count = count
4        self.keys = set()
5        self.prev = None
6        self.next = None
7
8
9class AllOne:
10
11    def __init__(self):
12        self.head = Node()
13        self.tail = Node()
14
15        self.head.next = self.tail
16        self.tail.prev = self.head
17
18        self.map = {}
19
20    def inc(self, key: str) -> None:
21        if key not in self.map:
22            node = self.head.next
23
24            if node == self.tail or node.count != 1:
25                new_node = Node(1)
26                self._insert_after(self.head, new_node)
27                node = new_node
28
29            node.keys.add(key)
30            self.map[key] = node
31
32        else:
33            node = self.map[key]
34            next_node = node.next
35
36            if next_node == self.tail or next_node.count != node.count + 1:
37                new_node = Node(node.count + 1)
38                self._insert_after(node, new_node)
39                next_node = new_node
40
41            next_node.keys.add(key)
42            self.map[key] = next_node
43
44            node.keys.remove(key)
45
46            if len(node.keys) == 0:
47                self._remove(node)
48
49    def dec(self, key: str) -> None:
50        node = self.map[key]
51
52        if node.count == 1:
53            del self.map[key]
54            node.keys.remove(key)
55
56            if len(node.keys) == 0:
57                self._remove(node)
58
59        else:
60            prev_node = node.prev
61
62            if prev_node == self.head or prev_node.count != node.count - 1:
63                new_node = Node(node.count - 1)
64                self._insert_after(prev_node, new_node)
65                prev_node = new_node
66
67            prev_node.keys.add(key)
68            self.map[key] = prev_node
69
70            node.keys.remove(key)
71
72            if len(node.keys) == 0:
73                self._remove(node)
74
75    def getMaxKey(self) -> str:
76        if self.tail.prev == self.head:
77            return ""
78
79        return next(iter(self.tail.prev.keys))
80
81    def getMinKey(self) -> str:
82        if self.head.next == self.tail:
83            return ""
84
85        return next(iter(self.head.next.keys))
86
87    def _insert_after(self, node, new_node):
88        new_node.prev = node
89        new_node.next = node.next
90
91        node.next.prev = new_node
92        node.next = new_node
93
94    def _remove(self, node):
95        node.prev.next = node.next
96        node.next.prev = node.prev
# Last updated: 8/22/2026, 12:12:05 PM
1class Codec:
2    def serialize(self, root: Optional[TreeNode]) -> str:
3        if root is None:
4            return ""
5        result = []
6        def preorder(node):
7            if node is None:
8                return
9            result.append(str(node.val))
10            preorder(node.left)
11            preorder(node.right)
12        preorder(root)
13        return ",".join(result)
14    def deserialize(self, data: str) -> Optional[TreeNode]:
15        if not data:
16            return None
17        values = list(map(int, data.split(",")))
18        index = 0
19        def build(min_val, max_val):
20            nonlocal index
21            if index == len(values):
22                return None
23            value = values[index]
24            if value < min_val or value > max_val:
25                return None
26            index += 1
27            node = TreeNode(value)
28            node.left = build(min_val, value - 1)
29            node.right = build(value + 1, max_val)
30            return node
31        return build(float("-inf"), float("inf"))
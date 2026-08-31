# Last updated: 8/31/2026, 1:58:59 PM
class Codec:
    def serialize(self, root: Optional[TreeNode]) -> str:
        if root is None:
            return ""
        result = []
        def preorder(node):
            if node is None:
                return
            result.append(str(node.val))
            preorder(node.left)
            preorder(node.right)
        preorder(root)
        return ",".join(result)
    def deserialize(self, data: str) -> Optional[TreeNode]:
        if not data:
            return None
        values = list(map(int, data.split(",")))
        index = 0
        def build(min_val, max_val):
            nonlocal index
            if index == len(values):
                return None
            value = values[index]
            if value < min_val or value > max_val:
                return None
            index += 1
            node = TreeNode(value)
            node.left = build(min_val, value - 1)
            node.right = build(value + 1, max_val)
            return node
        return build(float("-inf"), float("inf"))
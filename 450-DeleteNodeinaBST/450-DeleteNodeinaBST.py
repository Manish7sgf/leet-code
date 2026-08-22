# Last updated: 8/22/2026, 12:10:23 PM
1class Solution:
2    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
3        if root is None:
4            return None
5        if key < root.val:
6            root.left = self.deleteNode(root.left, key)
7        elif key > root.val:
8            root.right = self.deleteNode(root.right, key)
9        else:
10            if root.left is None:
11                return root.right
12            if root.right is None:
13                return root.left
14            temp = root.right
15            while temp.left:
16                temp = temp.left
17            root.val = temp.val
18            root.right = self.deleteNode(root.right, temp.val)
19        return root
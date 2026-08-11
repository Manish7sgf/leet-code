# Last updated: 8/11/2026, 11:49:58 AM
1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7class Solution:
8    def smallestFromLeaf(self, root: Optional[TreeNode]) -> str:
9        ans = None
10        def dfs(node, path):
11            nonlocal ans
12            if node is None:
13                return
14            path += chr(node.val + ord('a'))
15            if node.left is None and node.right is None:
16                s = path[::-1]
17                if ans is None or s < ans:
18                    ans = s
19                return
20            dfs(node.left, path)
21            dfs(node.right, path)
22        dfs(root, "")
23        return ans
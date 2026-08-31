# Last updated: 8/31/2026, 1:57:39 PM
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def smallestFromLeaf(self, root: Optional[TreeNode]) -> str:
        ans = None
        def dfs(node, path):
            nonlocal ans
            if node is None:
                return
            path += chr(node.val + ord('a'))
            if node.left is None and node.right is None:
                s = path[::-1]
                if ans is None or s < ans:
                    ans = s
                return
            dfs(node.left, path)
            dfs(node.right, path)
        dfs(root, "")
        return ans
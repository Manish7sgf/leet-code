# Last updated: 8/22/2026, 12:08:05 PM
1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7class Solution:
8    def isCompleteTree(self, root: Optional[TreeNode]) -> bool:
9        queue=deque([root])
10        while node:=queue.popleft():
11            queue.extend([node.left,node.right])
12        return not any(queue)
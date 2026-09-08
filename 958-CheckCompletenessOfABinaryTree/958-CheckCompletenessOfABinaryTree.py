# Last updated: 9/8/2026, 10:19:57 AM
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCompleteTree(self, root: Optional[TreeNode]) -> bool:
        queue=deque([root])
        while node:=queue.popleft():
            queue.extend([node.left,node.right])
        return not any(queue)
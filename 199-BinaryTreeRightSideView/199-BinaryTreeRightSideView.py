# Last updated: 8/31/2026, 1:59:36 PM
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if root is None: return []
        rv  = self.rightSideView(root.right)
        lv  = self.rightSideView(root.left)
        return [root.val]+rv+lv[len(rv):]
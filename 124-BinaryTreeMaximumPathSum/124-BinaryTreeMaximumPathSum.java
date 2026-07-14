// Last updated: 7/14/2026, 2:17:47 PM
/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
class Solution {
    public int maxPathSum(TreeNode root) {
        int res[]={root.val};
        dfs(root,res);
        return res[0];
    }
    private int dfs(TreeNode node,int res[])
    {
        if(node==null) return 0;
        int ls=Math.max(0,dfs(node.left,res));
        int rs=Math.max(0,dfs(node.right,res));
        res[0]=Math.max(res[0],ls+rs+node.val);
        return Math.max(ls,rs)+node.val;
    }
}
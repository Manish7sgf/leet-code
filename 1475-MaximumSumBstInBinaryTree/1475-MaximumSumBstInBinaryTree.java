// Last updated: 7/14/2026, 2:17:11 PM
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
    private static class Info {
        boolean isBST;
        int min;
        int max;
        int sum;
        Info(boolean isBST, int min, int max,int sum)
        {
            this.isBST=isBST;
            this.min=min;
            this.max=max;
            this.sum=sum;
        }
    }
    private int answer=0;
    public int maxSumBST(TreeNode root)
    {
        postOrder(root);
        return answer;
    }
    private Info postOrder(TreeNode node)
    {
        if(node==null)
        {
            return new Info(true,Integer.MAX_VALUE,Integer.MIN_VALUE,0);
        }
        Info left=postOrder(node.left);
        Info right=postOrder(node.right);
        if(!left.isBST||!right.isBST)
        {
            return new Info(false,0,0,0);
        }
        if(node.val<=left.max||node.val>=right.min)
        {
            return new Info(false,0,0,0);
        }
        int curSum=node.val+right.sum+left.sum;
        answer=Math.max(answer,curSum);
        int curMin=Math.min(node.val,left.min);
        int curMax=Math.max(node.val,right.max);
        return new Info(true,curMin,curMax,curSum);
    }
}
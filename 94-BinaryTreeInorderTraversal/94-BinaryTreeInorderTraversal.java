// Last updated: 7/14/2026, 2:17:55 PM
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
    void inorder(List<Integer>ans,TreeNode root)
    {
        if(root==null){
            return;
        }
        inorder(ans,root.left);
        ans.add(root.val);
        inorder(ans,root.right);
    }
    public List<Integer> inorderTraversal(TreeNode root) {
        List<Integer> ans=new ArrayList<>();
        inorder(ans,root);
        return ans;
    }
}
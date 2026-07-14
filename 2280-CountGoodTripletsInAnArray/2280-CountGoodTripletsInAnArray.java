// Last updated: 7/14/2026, 2:17:05 PM
class Solution {
    class BinaryTree
    {
        private int[] tree;
        private int n;
        public BinaryTree(int n)
        {
            this.n=n;
            this.tree=new int[n+1];
        }
        public void update(int i,int delta)
        {
            i=i+1;
            while(i<=n)
            {
                tree[i]=tree[i]+delta;
                i=i+(i&-i);
            }
        }
        public int query(int i)
        {
            if(i<0) return 0;
            i=i+1;
            int sum=0;
            while(i>0)
            {
                sum=sum+tree[i];
                i=i-(i&-i);
            }
            return sum;
        }
    }
    public long goodTriplets(int[] nums1, int[] nums2) {
        int n=nums1.length;
        int pos[]=new int[n];
        for(int i=0;i<n;i++)
        {
            pos[nums2[i]]=i;
        }
        long ans=0;
        BinaryTree tree=new BinaryTree(n);
        for(int num:nums1)
        {
            int p=pos[num];
            long left=tree.query(p-1);
            long pt=tree.query(n-1);
            long pu=tree.query(p);
            long right=(long)(n-1-p)-(pt-pu);
            ans=ans+left*right;
            tree.update(p,1);
        }
        return ans;
    }
}
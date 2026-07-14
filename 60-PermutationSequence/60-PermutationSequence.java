// Last updated: 7/14/2026, 2:18:12 PM
class Solution {
    public String getPermutation(int n, int k) {
        java.util.List<Integer> dig=new java.util.ArrayList<>();
        for(int i=1;i<=n;i++)
        {
            dig.add(i);
        }
        StringBuilder r=new StringBuilder();
        k-=1;
        int fact[]=new int[n];
        fact[0]=1;
        for(int i=1;i<n;i++)
        {
            fact[i]=fact[i-1]*i;
        }
        for(int i=n-1;i>=0;i--)
        {
            int gsize=fact[i];
            int idx=k/gsize;
            r.append(dig.get(idx));
            dig.remove(idx);
            k%=gsize;
        }
        return r.toString();
    }
}
// Last updated: 7/14/2026, 2:16:47 PM
class Solution {
    public long countMajoritySubarrays(int[] nums, int target) {
        int n=nums.length;
        boolean hasTarget=false;
        for(int x:nums)
        {
            if(x==target)
            {
                hasTarget=true;
                break;
            }
        }
        if(!hasTarget) return 0L;
        long pref[]=new long[n+1];
        for(int i=0;i<n;i++)
        {
            int val=(nums[i]==target) ? 1:-1;
            pref[i+1]=pref[i]+val;
        }
        long all[]=pref.clone();
        Arrays.sort(all);
        int m=0;
        for(int i=0;i<all.length;i++)
        {
            if(i==0|| all[i]!=all[i-1])
            {
                all[m++]=all[i];
            }
        }
        Fenwick bit=new Fenwick(m);
        long ans=0L;
        for(int k=0;k<=n;k++)
        {
            int idx=lowerBound(all,m,pref[k])+1;
            ans+=bit.query(idx-1);
            bit.update(idx,1);
        }
        return ans;
    }
    private int lowerBound(long all[],int m,long x)
    {
        int lo=0,hi=m;
        while(lo<hi)
        {
            int mid=(lo+hi)>>>1;
            if(all[mid]>=x) hi=mid;
            else lo=mid+1;
        }
        return lo;
    }
    static class Fenwick
    {
        long bit[];
        int n;
        Fenwick(int n)
        {
            this.n=n;
            this.bit=new long[n+1];
        }
        void update(int i,long delta)
        {
            while(i<=n)
            {
                bit[i]+=delta;
                i+=i&-i;
            }
        }
        long query(int i)
        {
            long sum=0;
            while(i>0)
            {
                sum+=bit[i];
                i-=i&-i;
            }
            return sum;
        }
    }
}
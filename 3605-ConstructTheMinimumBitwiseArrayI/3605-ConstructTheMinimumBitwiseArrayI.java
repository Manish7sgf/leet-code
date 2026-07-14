// Last updated: 7/14/2026, 2:16:59 PM
class Solution {
    public int[] minBitwiseArray(List<Integer> nums) {
        int n=nums.size();
        int a[]=new int[n];
        for(int i=0;i<n;i++)
        {
            int x=nums.get(i);
            if(x==2)
            {
                a[i]=-1;
                continue;
            }
            int result=x;
            for(int y=1;y<31;y++)
            {
                if(((x>>y)&1)==0)
                {
                    result=x^(1<<(y-1));
                    break;
                }
            }
            a[i]=result;
        }
        return a;
    }
}
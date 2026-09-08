// Last updated: 9/8/2026, 10:18:36 AM
class Solution {
    public int countMajoritySubarrays(int[] nums, int target) {
        int n=nums.length;
        int ans=0;
        for(int i=0;i<n;i++)
        {
            int cntTarget=0;
            for(int j=i;j<n ;j++)
            {
                if(nums[j]==target)
                {
                    cntTarget++;
                }
                int len=j-i+1;
                if(cntTarget*2>len)
                {
                    ans++;
                }
            }
        }
        return ans;
    }
}
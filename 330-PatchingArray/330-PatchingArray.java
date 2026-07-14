// Last updated: 7/14/2026, 2:17:29 PM
class Solution {
    public int minPatches(int[] nums, int n) {
        long miss=1;
        int patch=0;
        int i=0;
        while(miss<=n)
        {
            if(i<nums.length && nums[i]<=miss)
            {
                miss+=nums[i];
                i++;
            }
            else
            {
                miss+=miss;
                patch++;
            }
        }
        return patch;
    }
}
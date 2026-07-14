// Last updated: 7/14/2026, 2:18:25 PM
class Solution {
    public int removeDuplicates(int[] nums) {
        int j=0;
        for(int i=1;i<nums.length;i++)
        {
            if(nums[j]!=nums[i])
            {
                nums[++j]=nums[i];
            }
        }
        return ++j;
    }
}
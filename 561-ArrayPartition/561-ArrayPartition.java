// Last updated: 7/14/2026, 2:17:24 PM
class Solution {
    public int arrayPairSum(int[] nums) {
        Arrays.sort(nums);
        int sum=0;
        for(int i=0;i<nums.length;i+=2)
        {
            sum+=nums[i];
        }
        return sum;
    }
}
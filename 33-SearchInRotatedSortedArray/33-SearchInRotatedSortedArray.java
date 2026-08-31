// Last updated: 8/31/2026, 2:01:08 PM
class Solution {
    public int search(int[] nums, int target) {
        int s=0,end=nums.length-1;
        while(s<=end)
        {
            int mid=s+(end-s)/2;
            if(nums[mid]==target) return mid;
            if(nums[mid]>=nums[s]){
                if(target>=nums[s]&&target<nums[mid])
                {
                    end=mid-1;
                }
                else
                {
                    s=mid+1;
                }
            }
            else
            {
                if(target>nums[mid]&&target<=nums[end])
                {
                    s=mid+1;
                }
                else end=mid-1;
            }
        }
        return -1;
    }
}
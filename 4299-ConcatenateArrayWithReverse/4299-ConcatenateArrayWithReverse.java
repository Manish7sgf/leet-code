// Last updated: 7/14/2026, 2:16:50 PM
class Solution {
    public int[] concatWithReverse(int[] nums) {
        int n=nums.length;
        int rev[]=new int[2*n];
        for(int i=0;i<n;i++)
        {
            rev[i]=nums[i];
        }
        for(int i=0;i<n;i++)
        {
            rev[i+n]=nums[n-i-1];
        }
        return rev;
    }
}
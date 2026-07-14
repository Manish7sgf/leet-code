// Last updated: 7/14/2026, 2:18:44 PM
class Solution {
    public double findMedianSortedArrays(int[] nums1, int[] nums2) {
        if(nums1.length>nums2.length){
            return findMedianSortedArrays(nums2,nums1);
        }
        int m=nums1.length;
        int n=nums2.length;
        int low=0,high=m;
        while(low<=high)
        {
            int p1=(low+high)/2;
            int p2=(m+n+1)/2-p1;
            int maxLeft1=(p1==0)?Integer.MIN_VALUE:nums1[p1-1];
            int minRight1=(p1==m)?Integer.MAX_VALUE:nums1[p1];
            int maxLeft2=(p2==0)?Integer.MIN_VALUE:nums2[p2-1];
            int minRight2=(p2==n)?Integer.MAX_VALUE:nums2[p2];
            if(maxLeft1<=minRight2 && maxLeft2<=minRight1)
            {
                if((m+n)%2==0)
                {
                    return (Math.max(maxLeft1,maxLeft2)+Math.min(minRight1,minRight2))/2.0;
                }
                else
                {
                    return Math.max(maxLeft1,maxLeft2);
                }
            }
            else if(maxLeft1>minRight2){
                high=p1-1;
            }
            else{
                low=p1+1;
            }
        }
        return 0.0;
    }
}
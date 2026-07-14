// Last updated: 7/14/2026, 2:17:58 PM
class Solution {
    public void merge(int[] nums1, int m, int[] nums2, int n) {
        for(int j=0,i=m;j<n;j++)
        {
            nums1[i]=nums2[j];
            i++;
        }
        Arrays.sort(nums1);
    }
}
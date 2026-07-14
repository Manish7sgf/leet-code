// Last updated: 7/14/2026, 2:17:25 PM
class Solution {
    public int minMoves(int[] nums) {
        int min=Integer.MAX_VALUE;
        for(int n:nums) min=Math.min(min,n);
        int m=0;
        for(int n:nums) m+=n-min;
        return m;
    }
}
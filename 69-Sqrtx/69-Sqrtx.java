// Last updated: 7/14/2026, 2:18:07 PM
class Solution {
    public int mySqrt(int x) {
       if(x<2) return x; 
       int low=1,high=x,ans=0;
        while(low<=high)
        {
            int  mid=low+(high-low)/2;
             if (mid <= x / mid) {
                ans = mid;     
                low = mid + 1; 
            } else {
                high = mid - 1;
            }
        }
        return ans;
    }
}
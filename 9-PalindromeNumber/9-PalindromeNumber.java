// Last updated: 7/14/2026, 2:18:38 PM
class Solution {
    public boolean isPalindrome(int x) {
        if(x<0) return false;
        int rev=0;
        int temp=x;
        while(x>0){
            int a= x % 10;
            rev= rev*10 + a;
            x/=10;
        }
        if(temp==rev)
            return true;
        return false;
    }
}
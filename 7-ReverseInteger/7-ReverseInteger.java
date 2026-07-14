// Last updated: 7/14/2026, 2:18:39 PM
class Solution {
    public int reverse(int x) {
        int rev=0;
        while(x!=0)
        {
            int temp=x%10;
            x=x/10;
            if(rev>214748364||rev<-214748364) return 0;
            rev=rev*10+temp;
        }
        return rev;
    }
}
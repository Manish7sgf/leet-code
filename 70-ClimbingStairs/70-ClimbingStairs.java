// Last updated: 7/14/2026, 2:18:04 PM
class Solution 
{
    public int climbStairs(int n) 
    {
        int p1=1,p2=1;
        for(int i=2;i<=n;i++)
        {
            int temp=p1+p2;
            p2=p1;
            p1=temp;
        }
        return p1;
    }
}
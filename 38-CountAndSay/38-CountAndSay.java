// Last updated: 7/14/2026, 2:18:18 PM
class Solution {
    public String countAndSay(int n) {
        if(n==1) return "1";
        String r="1";
        for(int i=2;i<=n;i++)
        {
            r=rle(r);
        }
        return r;
    }
    private String rle(String s)
    {
        StringBuilder sb=new StringBuilder();
        int c=1;
        for(int i=1;i<s.length();i++)
        {
            if(s.charAt(i)==s.charAt(i-1)) c++;
            else
            {
                sb.append(c).append(s.charAt(i-1));
                c=1;
            }
        }
        sb.append(c).append(s.charAt(s.length() - 1));
        return sb.toString();
    }
}
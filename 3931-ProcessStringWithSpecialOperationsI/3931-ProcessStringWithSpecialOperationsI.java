// Last updated: 7/14/2026, 2:16:58 PM
class Solution {
    public String processStr(String s) {
        StringBuilder sb=new StringBuilder();
        for(char ch:s.toCharArray())
        {
            if('a'<=ch || 'z'<=ch) sb.append(ch);
            else if (ch=='#')
            {
                String c=sb.toString();
                sb.append(c);
            }
            else if(ch=='*')
            {
                if(sb.length()>0) sb.deleteCharAt(sb.length()-1);
            }
            else if(ch=='%') sb.reverse();
        }
        return sb.toString();
    }
}
// Last updated: 7/14/2026, 2:17:33 PM
class Solution {
    public boolean isAnagram(String s, String t) {
        if(s.length()!=t.length()) return false;
        int c[]=new int[256];
        for(int i=0;i<s.length();i++)
        {
            c[s.charAt(i)]++;
        }
        for(int i=0;i<t.length();i++) c[t.charAt(i)]--;
        for(int i=0;i<256;i++)
        {
            if(c[i]!=0) return false;
        }
        return true;
    }
}
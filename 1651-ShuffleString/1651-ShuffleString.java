// Last updated: 7/14/2026, 2:17:10 PM
class Solution {
    public String restoreString(String s, int[] indices) {
        char[]ch=s.toCharArray();
        char[]ans=new char[indices.length];
        for(int i=0;i<s.length();i++){
            ans[indices[i]]=ch[i];
        }
        return new String(ans);
    }
}
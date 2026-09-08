// Last updated: 9/8/2026, 10:19:33 AM
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
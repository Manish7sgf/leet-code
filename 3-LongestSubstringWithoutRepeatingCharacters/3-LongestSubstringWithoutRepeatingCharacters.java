// Last updated: 7/14/2026, 2:18:45 PM
class Solution {
    public int lengthOfLongestSubstring(String s) {
        int n=s.length();
        int maxlen=0;
        Set<Character> charset=new HashSet<>();
        int l=0;
        for(int r=0;r<n;r++)
        {
            if(!charset.contains(s.charAt(r)))
            {
                charset.add(s.charAt(r));
                maxlen=Math.max(maxlen,r-l+1);
            }
            else
            {
                while(charset.contains(s.charAt(r)))
                {
                    charset.remove(s.charAt(l));
                    l++;
                }
                charset.add(s.charAt(r));
            }
        }
        return maxlen;
    }
}
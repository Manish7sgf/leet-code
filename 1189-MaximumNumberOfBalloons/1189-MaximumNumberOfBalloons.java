// Last updated: 9/8/2026, 10:19:48 AM
class Solution {
    public int maxNumberOfBalloons(String text) {
        int freq[]=new int[26];
        for(int i=0;i<text.length();i++)
        {
            char c=text.charAt(i);
            if(c=='b'||c=='a'||c=='l'||c=='o'||c=='n')
            {
                freq[c-'a']++;
            }
        }
        int cB=freq['b'-'a'];
        int cA=freq['a'-'a'];
        int cL=freq['l'-'a']/2;
        int cO=freq['o'-'a']/2;
        int cN=freq['n'-'a'];
        return Math.min(Math.min(cB, cA), Math.min(Math.min(cL, cO), cN));
    }
}
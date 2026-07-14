// Last updated: 7/14/2026, 2:16:46 PM
class Solution {
    public String mapWordWeights(String[] words, int[] weights) {
        StringBuilder r=new StringBuilder();
        for(String word:words)
        {
            int wordWeight=0;
            for(char c:word.toCharArray())
            {
                wordWeight+=weights[c-'a'];
            }
            int mapped=wordWeight % 26;
            char mappedChar=(char)('z'-mapped);
            r.append(mappedChar);
        }
        return r.toString();
    }
}
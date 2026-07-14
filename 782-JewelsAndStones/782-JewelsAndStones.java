// Last updated: 7/14/2026, 2:17:16 PM
class Solution {
    public int numJewelsInStones(String jewels, String stones) {
        int count =0;
        for (char j:jewels.toCharArray()){
            for(char s:stones.toCharArray()){
                if (s==j){
                    count++;
                }
             
            }
           
        }
        return count;
    }
}
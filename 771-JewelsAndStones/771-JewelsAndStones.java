// Last updated: 9/8/2026, 10:20:15 AM
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
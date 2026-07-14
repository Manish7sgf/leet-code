// Last updated: 7/14/2026, 2:17:07 PM
class Solution {
    public boolean isSameAfterReversals(int num) {
        if(num==0) return true;
        if(!(num%10==0)) return true;
        return false;
    }
}
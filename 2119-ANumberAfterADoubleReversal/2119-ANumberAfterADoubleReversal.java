// Last updated: 9/8/2026, 10:19:21 AM
class Solution {
    public boolean isSameAfterReversals(int num) {
        if(num==0) return true;
        if(!(num%10==0)) return true;
        return false;
    }
}
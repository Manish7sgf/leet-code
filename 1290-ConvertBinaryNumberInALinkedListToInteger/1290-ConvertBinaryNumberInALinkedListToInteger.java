// Last updated: 9/8/2026, 10:19:40 AM
/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    public int getDecimalValue(ListNode head) {
        ListNode temp=head;
        String s="";
        while(temp!=null){
            s+=temp.val;
            temp=temp.next;
        }
        int n=Integer.parseInt(s,2);
        return n;
    }
}
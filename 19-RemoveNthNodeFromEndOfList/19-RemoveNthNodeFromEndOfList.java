// Last updated: 7/14/2026, 2:18:31 PM
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
    public ListNode removeNthFromEnd(ListNode head, int n) {
        ListNode dum=new ListNode(-1);
        dum.next=head;
        ListNode firstptr=dum;
        ListNode secondptr=dum;
        for(int i=0;i<=n;i++){
            secondptr=secondptr.next;
        }
         while (secondptr != null) {
            firstptr = firstptr.next;
            secondptr = secondptr.next;
        }
            firstptr.next=firstptr.next.next;
            return dum.next;
       
    }
}
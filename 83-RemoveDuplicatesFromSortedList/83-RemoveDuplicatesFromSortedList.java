// Last updated: 7/14/2026, 2:17:59 PM
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
    public ListNode deleteDuplicates(ListNode head) {
        if(head == null || head.next ==null) return head;
        ListNode cur=head;
        while(cur!=null && cur.next!=null)
        {
            if(cur.val==cur.next.val) cur.next=cur.next.next;
            else cur=cur.next;
        }
        return head;
    }
}
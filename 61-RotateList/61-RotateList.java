// Last updated: 7/14/2026, 2:18:11 PM
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
    public ListNode rotateRight(ListNode head, int k) {
        if (head == null) return head;
        int len = 1;
        ListNode temp = head;
        while (temp.next != null) 
        {
            temp = temp.next;
            len++;
        }
        int pos = k % len;
        if (pos==0) 
        return head;
        ListNode current = head;
        for (int i = 0;i<len - pos - 1; i++) 
        {
            current = current.next;
        }

        ListNode newHead = current.next;
        current.next = null;
        temp.next = head;

        return newHead;
    }
}
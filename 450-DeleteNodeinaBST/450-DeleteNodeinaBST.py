# Last updated: 8/24/2026, 12:17:56 PM
1"""
2# Definition for a Node.
3class Node:
4    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
5        self.val = int(x)
6        self.next = next
7        self.random = random
8"""
9
10class Solution:
11    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
12        if head is None:
13            return None
14        mp={}
15        curr=head
16        while curr:
17            mp[curr]=Node(curr.val)
18            curr=curr.next
19        curr=head
20        while curr:
21            mp[curr].next= mp.get(curr.next)
22            mp[curr].random=mp.get(curr.random)
23            curr=curr.next
24        return mp[head]
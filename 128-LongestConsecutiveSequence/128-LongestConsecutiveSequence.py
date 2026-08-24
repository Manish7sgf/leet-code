# Last updated: 8/24/2026, 11:48:14 AM
1class Solution:
2    def longestConsecutive(self, nums: List[int]) -> int:
3        s=set(nums)
4        longest=0
5        for i in s:
6            if i-1 not in s:
7                curr=i
8                length=1
9                while curr+1 in s:
10                    curr+=1
11                    length+=1
12                longest=max(longest,length)
13        return longest
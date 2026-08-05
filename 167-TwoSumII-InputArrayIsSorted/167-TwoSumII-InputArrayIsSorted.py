# Last updated: 8/5/2026, 1:37:43 PM
1class Solution:
2    def twoSum(self, numbers: List[int], target: int) -> List[int]:
3        l=0
4        r=len(numbers)-1
5        while l<r:
6            curr_sum=numbers[l]+numbers[r]
7            if curr_sum==target:
8                return [l+1,r+1]
9            elif curr_sum<target:
10                l+=1
11            else:
12                r-=1
13        return [-1,-1]
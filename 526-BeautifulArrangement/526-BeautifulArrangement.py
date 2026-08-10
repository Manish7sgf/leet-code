# Last updated: 8/10/2026, 11:37:42 AM
1class Solution:
2    def isPossible(self, nums: List[int]) -> bool:
3        count = {}
4        for num in nums:
5            count[num] = count.get(num, 0) + 1
6        end = {}
7        for num in nums:
8            if count[num] == 0:
9                continue
10            count[num] -= 1
11            if end.get(num - 1, 0) > 0:
12                end[num - 1] -= 1
13                end[num] = end.get(num, 0) + 1
14            elif count.get(num + 1, 0) > 0 and count.get(num + 2, 0) > 0:
15                count[num + 1] -= 1
16                count[num + 2] -= 1
17                end[num + 2] = end.get(num + 2, 0) + 1
18            else:
19                return False
20        return True
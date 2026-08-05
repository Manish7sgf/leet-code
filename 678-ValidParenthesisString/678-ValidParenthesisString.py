# Last updated: 8/5/2026, 2:45:14 PM
1class Solution:
2    def countArrangement(self, n: int) -> int:
3        used = [False] * (n + 1)
4        def backtrack(pos):
5            if pos > n:
6                return 1
7            c=0
8            for i in range(1, n + 1):
9                if not used[i] and (i % pos == 0 or pos % i == 0):
10                    used[i] = True
11                    c+=backtrack(pos + 1)
12                    used[i]=False
13            return c
14        return backtrack(1)
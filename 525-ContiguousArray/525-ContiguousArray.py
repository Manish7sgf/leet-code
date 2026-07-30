# Last updated: 7/30/2026, 12:05:40 PM
1class Solution:
2    def strWithout3a3b(self, a: int, b: int) -> str:
3        ans = []
4        while a > 0 or b > 0:
5            if (a >= b and not (len(ans) >= 2 and ans[-1] == ans[-2] == 'a')) \
6               or (len(ans) >= 2 and ans[-1] == ans[-2] == 'b'):
7                ans.append('a')
8                a -= 1
9            else:
10                ans.append('b')
11                b -= 1
12        return "".join(ans)
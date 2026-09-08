# Last updated: 9/8/2026, 10:19:51 AM
class Solution:
    def strWithout3a3b(self, a: int, b: int) -> str:
        ans = []
        while a > 0 or b > 0:
            if (a >= b and not (len(ans) >= 2 and ans[-1] == ans[-2] == 'a')) \
               or (len(ans) >= 2 and ans[-1] == ans[-2] == 'b'):
                ans.append('a')
                a -= 1
            else:
                ans.append('b')
                b -= 1
        return "".join(ans)
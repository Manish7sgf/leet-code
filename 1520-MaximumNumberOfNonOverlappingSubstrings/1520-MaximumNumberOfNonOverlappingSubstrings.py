# Last updated: 9/19/2026, 11:45:22 AM
class Solution:
    def maxNumOfSubstrings(self, s: str) -> List[str]:
        first = [len(s)] * 26
        last = [-1] * 26
        for i, ch in enumerate(s):
            x = ord(ch) - ord('a')
            first[x] = min(first[x], i)
            last[x] = i
        intervals = []
        for x in range(26):
            if last[x] == -1:
                continue
            l = first[x]
            r = last[x]
            i = l
            while i <= r:
                c = ord(s[i]) - ord('a')
                if first[c] < l:
                    break
                r = max(r, last[c])
                i += 1
            else:
                intervals.append((l, r))
        intervals.sort(key=lambda x: x[1])
        ans = []
        end = -1
        for l, r in intervals:
            if l > end:
                ans.append(s[l:r + 1])
                end = r
        return ans
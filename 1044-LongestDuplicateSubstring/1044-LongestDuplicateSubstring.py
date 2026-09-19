# Last updated: 9/19/2026, 11:45:36 AM
class Solution:
    def longestDupSubstring(self, s: str) -> str:
        n = len(s)
        def search(length):
            base = 26
            mod = (1 << 61) - 1
            h = 0
            power = pow(base, length - 1, mod)
            seen = set()
            for i in range(length):
                h = (h * base + (ord(s[i]) - ord('a'))) % mod
            seen.add(h)
            for i in range(length, n):
                h = (
                    h
                    - (ord(s[i - length]) - ord('a')) * power
                ) % mod
                h = (h * base + (ord(s[i]) - ord('a'))) % mod
                if h in seen:
                    return i - length + 1
                seen.add(h)
            return -1
        left = 1
        right = n - 1
        start = -1
        length = 0
        while left <= right:
            mid = (left + right) // 2
            pos = search(mid)
            if pos != -1:
                length = mid
                start = pos
                left = mid + 1
            else:
                right = mid - 1
        if start == -1:
            return ""
        return s[start:start + length]
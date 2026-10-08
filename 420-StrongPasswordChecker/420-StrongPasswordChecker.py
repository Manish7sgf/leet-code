# Last updated: 10/8/2026, 10:33:43 AM
class Solution:
    def strongPasswordChecker(self, password: str) -> int:
        n = len(password)
        missing = 3
        if any(c.islower() for c in password):
            missing -= 1
        if any(c.isupper() for c in password):
            missing -= 1
        if any(c.isdigit() for c in password):
            missing -= 1

        replace = 0
        groups = [0, 0, 0]
        i = 0

        while i < n:
            j = i
            while j < n and password[j] == password[i]:
                j += 1
            length = j - i
            if length >= 3:
                replace += length // 3
                groups[length % 3] += 1
            i = j

        if n < 6:
            return max(missing, 6 - n)

        if n <= 20:
            return max(missing, replace)

        delete = n - 20

        use = min(delete, groups[0])
        delete -= use
        replace -= use

        use = min(delete, groups[1] * 2)
        delete -= use
        replace -= use // 2

        replace -= delete // 3

        return n - 20 + max(missing, replace)
# Last updated: 10/13/2026, 9:15:14 AM
class Solution:
    def letterCombinations(self, digits: str) -> list[str]:

        if not digits:
            return []

        phone = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }

        result = []

        def backtrack(index, path):
            if index == len(digits):
                result.append("".join(path))
                return

            letters = phone[digits[index]]

            for letter in letters:
                path.append(letter)
                backtrack(index + 1, path)
                path.pop()

        backtrack(0, [])
        return result
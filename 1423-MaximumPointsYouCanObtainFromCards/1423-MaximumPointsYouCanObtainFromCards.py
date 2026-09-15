# Last updated: 9/15/2026, 11:07:37 AM
class Solution:
    def maxScore(self, cardPoints, k):
        n = len(cardPoints)
        tot = sum(cardPoints)
        win = n - k
        curr = sum(cardPoints[:win])
        minimum = curr
        for i in range(win, n):
            curr += cardPoints[i]
            curr -= cardPoints[i - win]
            minimum = min(minimum, curr)
        return tot - minimum
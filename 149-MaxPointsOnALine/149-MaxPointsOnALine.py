# Last updated: 8/31/2026, 1:59:51 PM
class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        if len(points) <= 2:
            return len(points)
        ans = 0
        for i in range(len(points)):
            slopes = {}
            for j in range(i + 1, len(points)):
                x1, y1 = points[i]
                x2, y2 = points[j]
                dx = x2 - x1
                dy = y2 - y1
                if dx == 0:
                    slope = "vertical"
                else:
                    g = gcd(dx, dy)
                    dx //= g
                    dy //= g
                    if dx < 0:
                        dx = -dx
                        dy = -dy

                    slope = (dy, dx)
                slopes[slope] = slopes.get(slope, 0) + 1
                ans = max(ans, slopes[slope] + 1)
        return ans
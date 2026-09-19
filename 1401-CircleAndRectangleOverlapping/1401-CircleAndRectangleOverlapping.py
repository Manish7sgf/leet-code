# Last updated: 9/19/2026, 11:45:27 AM
class Solution:
    def checkOverlap(self, radius: int, xCenter: int, yCenter: int, x1: int, y1: int, x2: int, y2: int) -> bool:
        x=max(x1,min(xCenter,x2))-xCenter
        y=max(y1,min(yCenter,y2))-yCenter
        return x*x+y*y<=radius*radius
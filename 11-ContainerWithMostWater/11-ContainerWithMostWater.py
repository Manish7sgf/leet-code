# Last updated: 7/14/2026, 2:18:36 PM
class Solution(object):
    def maxArea(self, height):
        left=0
        right=len(height)-1
        max_w=0
        while left<right:
            width=right-left
            h=min(height[left],height[right])
            a=width*h
            max_w=max(max_w,a)
            if height[left]<height[right]:
                left+=1
            else:
                right-=1
        return max_w
        
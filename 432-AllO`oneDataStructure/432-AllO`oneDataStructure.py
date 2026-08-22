# Last updated: 8/22/2026, 10:16:50 AM
1class Solution:
2    def threeSum(self, nums: List[int]) -> List[List[int]]:
3        nums.sort()
4        result = []
5        for i in range(len(nums) - 2):
6            if i > 0 and nums[i] == nums[i - 1]:
7                continue
8            left = i + 1
9            right = len(nums) - 1
10            while left < right:
11                total = nums[i] + nums[left] + nums[right]
12                if total == 0:
13                    result.append([nums[i], nums[left], nums[right]])
14                    while left < right and nums[left] == nums[left + 1]:
15                        left += 1
16                    while left < right and nums[right] == nums[right - 1]:
17                        right -= 1
18                    left += 1
19                    right -= 1
20                elif total < 0:
21                    left += 1
22                else:
23                    right -= 1
24        return result
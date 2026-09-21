# Last updated: 9/21/2026, 11:20:12 AM
class Solution:
    def firstMissingPositive(self, nums: list[int]) -> int:
        def swap(arr,i,j):
            arr[i],arr[j]=arr[j],arr[i]
        n=len(nums)
        for i in range(n):
            while 0<nums[i]<=n and nums[nums[i]-1]!=nums[i]:
                swap(nums,i,nums[i]-1)
        for i in range(n):
            if nums[i]!=i+1:
                return i+1
        return n+1
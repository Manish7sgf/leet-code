# Last updated: 9/30/2026, 9:42:53 AM
class Solution:
    def smallestDistancePair(self, nums: List[int], k: int) -> int:
        nums.sort()
        minDis,maxDis=0,nums[-1]-nums[0]
        while minDis<maxDis:
            midDis=(minDis+maxDis)//2
            if self.countDis(nums,midDis)<k:
                minDis=midDis+1
            else:
                maxDis=midDis
        return minDis
    def countDis(self,nums:List[int],targetDis:int) -> int:
        c=l=0
        for r in range(1,len(nums)):
            while nums[r]-nums[l]>targetDis:
                l+=1
            c+=r-l
        return c
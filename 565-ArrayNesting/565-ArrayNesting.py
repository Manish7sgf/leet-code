# Last updated: 8/31/2026, 1:58:35 PM
class Solution:
    def arrayNesting(self, nums: List[int]) -> int:
        res=0
        l=len(nums)
        gset=set()
        for k in range(l):
            if k not in gset:
                currlen,currset,val=0,set(),k
                while True:
                    if nums[val] in currset: break
                    currset.add(nums[val])
                    gset.add(nums[val])
                    currlen,val=currlen+1,nums[val]
                res=max(res,currlen)
        return res
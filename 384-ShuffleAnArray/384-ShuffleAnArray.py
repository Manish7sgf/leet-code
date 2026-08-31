# Last updated: 8/31/2026, 1:59:09 PM
class Solution:

    def __init__(self, nums: List[int]):
        self.dup=nums[:]
        self.nums=nums
        self.l=len(nums)

    def reset(self) -> List[int]:
        self.nums[:]=self.dup
        return self.nums

    def shuffle(self) -> List[int]:
        arr=self.nums
        for i in range(self.l):
            j=randint(i,self.l-1)
            arr[i],arr[j]=arr[j],arr[i]
        return arr

# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()
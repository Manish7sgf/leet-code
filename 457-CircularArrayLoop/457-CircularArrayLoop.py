# Last updated: 8/31/2026, 1:58:52 PM
class Solution:
    def circularArrayLoop(self, nums: List[int]) -> bool:
        n = len(nums)
        def next(i):
            return (i+nums[i])%n
        for i in range(n):
            if nums[i]==0:
                continue
            slow=i
            fast=i
            d= nums[i]>0
            while True:
                if (nums[slow]>0)!=d:
                    break
                if (nums[fast]>0)!=d:
                    break
                next_fast = next(fast)
                if (nums[next_fast] > 0) != d:
                    break
                slow = next(slow)
                fast = next(next_fast)
                if slow == fast:
                    if slow == next(slow):
                        break
                    return True
            j = i
            while (nums[j] > 0)==d and nums[j] != 0:
                nxt = next(j)
                nums[j]=0
                j = nxt
        return False
# Last updated: 7/14/2026, 2:16:52 PM
class Solution:
    def maxTotalValue(self, nums: List[int], k: int) -> int:
        n=len(nums)
        log=(n).bit_length()
        log2=[0]*(n+1)
        for i in range(2,n+1):
            log2[i]=log2[i//2]+1
        st_max=[[0]*log for _ in range(n)]
        st_min=[[0]*log for _ in range(n)]
        for i in range(n):
            st_max[i][0]=nums[i]
            st_min[i][0]=nums[i]
        j=1
        while(1<<j) <=n:
            length=1 << j
            half=length >> 1
            for i in range(0,n-length+1):
                st_max[i][j]=max(st_max[i][j-1],st_max[i+half][j-1])
                st_min[i][j]=min(st_min[i][j-1],st_min[i+half][j-1])
            j+=1
        
        def get_max(l:int,r:int) -> int:
            length=r-l+1
            j=log2[length]
            return max(st_max[l][j],st_max[r-(1<<j)+1][j])
        def get_min(l:int,r:int) -> int:
            length=r-l+1
            j=log2[length]
            return min(st_min[l][j],st_min[r-(1<<j)+1][j])
        def value(l:int,r:int)->int:
            return get_max(l,r) - get_min(l,r)
        
        heap=[]
        for l in range(0,n):
            r=n-1
            v=value(l,r)
            heapq.heappush(heap,(-v,l,r))
        ans=0
        for _ in range(k):
            neg_v,l,r=heapq.heappop(heap)
            v=-neg_v
            ans+=v
            if r>l:
                r2=r-1
                v2=value(l,r2)
                heapq.heappush(heap,(-v2,l,r2))
        return ans
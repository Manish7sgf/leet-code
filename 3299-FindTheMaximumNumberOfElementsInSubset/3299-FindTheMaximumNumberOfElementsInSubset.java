// Last updated: 7/14/2026, 2:17:01 PM
class Solution {
    public int maximumLength(int[] nums) {
        Map<Long,Integer> freq=new HashMap<>();
        for(int num:nums)
        {
            long x=num;
            freq.put(x,freq.getOrDefault(x,0)+1);
        }
        int ans=1;
        int cnt1=freq.getOrDefault(1L,0);
        if(cnt1>0)
        {
            ans=Math.max(ans,(cnt1%2==1) ? cnt1:cnt1-1);
        }
        for(long x:freq.keySet())
        {
            if(x==1L) continue;
            List<Long> chain=new ArrayList<>();
            long cur=x;
            for(int i=0;i<10;i++)
            {
                if(cur>1_000_000_000L) break;
                if(!freq.containsKey(cur)) break;
                chain.add(cur);
                if(cur>1_000_000_000L/cur) break;
                cur=cur*cur;
            }
            for(int i=0;i<chain.size();i++)
            {
                boolean ok=true;
                for(int j=0;j<i;j++)
                {
                    if(freq.get(chain.get(j))<2)
                    {
                        ok=false;
                        break;
                    }
                }
                if(ok&&freq.get(chain.get(i))>=1)
                {
                    ans=Math.max(ans,2*i+1);
                }
            }
        }
        return ans;
    }
}
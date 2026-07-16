// Last updated: 7/16/2026, 11:12:03 AM
1class Solution {
2    public int search(int[] nums, int target) {
3        int s=0,end=nums.length-1;
4        while(s<=end)
5        {
6            int mid=s+(end-s)/2;
7            if(nums[mid]==target) return mid;
8            if(nums[mid]>=nums[s]){
9                if(target>=nums[s]&&target<nums[mid])
10                {
11                    end=mid-1;
12                }
13                else
14                {
15                    s=mid+1;
16                }
17            }
18            else
19            {
20                if(target>nums[mid]&&target<=nums[end])
21                {
22                    s=mid+1;
23                }
24                else end=mid-1;
25            }
26        }
27        return -1;
28    }
29}
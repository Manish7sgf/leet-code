# Last updated: 9/1/2026, 11:55:08 AM
1class TimeMap:
2    def __init__(self):
3        self.store = {}
4    def set(self,key:str,value:str,timestamp:int) -> None:
5        if key not in self.store:
6            self.store[key] = []
7        self.store[key].append((timestamp, value))
8    def get(self, key: str, timestamp: int) -> str:
9        if key not in self.store:
10            return ""
11        values = self.store[key]
12        left = 0
13        right = len(values) - 1
14        ans = ""
15        while left <= right:
16            mid = (left + right) // 2
17            if values[mid][0] <= timestamp:
18                ans = values[mid][1]
19                left = mid + 1
20            else:
21                right = mid - 1
22        return ans
23
24# Your TimeMap object will be instantiated and called as such:
25# obj = TimeMap()
26# obj.set(key,value,timestamp)
27# param_2 = obj.get(key,timestamp)
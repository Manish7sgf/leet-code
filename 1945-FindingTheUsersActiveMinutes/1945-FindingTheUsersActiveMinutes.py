# Last updated: 9/1/2026, 12:32:30 PM
class Solution:
    def findingUsersActiveMinutes(self, logs: List[List[int]], k: int) -> List[int]:
        users = {}
        for user, minute in logs:
            if user not in users:
                users[user] = set()
            users[user].add(minute)
        ans = [0] * k
        for user in users:
            count = len(users[user])
            if count <= k:
                ans[count - 1] += 1
        return ans
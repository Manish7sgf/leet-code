# Last updated: 8/31/2026, 1:57:22 PM
class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        positions = []
        prev = head
        curr = head.next
        index = 1
        while curr and curr.next:
            if (curr.val > prev.val and curr.val > curr.next.val) or \
               (curr.val < prev.val and curr.val < curr.next.val):
                positions.append(index)
            prev = curr
            curr = curr.next
            index += 1
        if len(positions) < 2:
            return [-1, -1]
        minimum = float('inf')
        for i in range(1, len(positions)):
            minimum = min(minimum, positions[i] - positions[i - 1])
        maximum = positions[-1] - positions[0]
        return [minimum, maximum]
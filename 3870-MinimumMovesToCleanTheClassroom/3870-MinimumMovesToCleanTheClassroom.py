# Last updated: 9/1/2026, 12:00:57 PM
from collections import deque
class Solution:
    def minMoves(self, classroom: List[str], energy: int) -> int:
        m = len(classroom)
        n = len(classroom[0])
        litter = []
        start = None
        for i in range(m):
            for j in range(n):
                if classroom[i][j] == 'S':
                    start = (i, j)
                elif classroom[i][j] == 'L':
                    litter.append((i, j))
        litter_index = {}
        for i in range(len(litter)):
            litter_index[litter[i]] = i
        all_collected = (1 << len(litter)) - 1
        queue = deque()
        queue.append((start[0], start[1], 0, energy, 0))
        visited = set()
        visited.add((start[0], start[1], 0, energy))
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        while queue:
            r, c, mask, remaining, moves = queue.popleft()
            if mask == all_collected:
                return moves
            for dr, dc in directions:
                nr = r + dr
                nc = c + dc
                if nr < 0 or nr >= m or nc < 0 or nc >= n:
                    continue
                if classroom[nr][nc] == 'X':
                    continue
                if remaining == 0:
                    continue
                new_energy = remaining - 1
                new_mask = mask
                if classroom[nr][nc] == 'L':
                    bit = litter_index[(nr, nc)]
                    new_mask |= (1 << bit)
                if classroom[nr][nc] == 'R':
                    new_energy = energy
                state = (nr, nc, new_mask, new_energy)
                if state not in visited:
                    visited.add(state)
                    queue.append((nr, nc, new_mask, new_energy, moves + 1))
        return -1
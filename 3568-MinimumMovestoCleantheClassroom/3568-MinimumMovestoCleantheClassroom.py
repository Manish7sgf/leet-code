# Last updated: 9/1/2026, 11:58:55 AM
1from collections import deque
2class Solution:
3    def minMoves(self, classroom: List[str], energy: int) -> int:
4        m = len(classroom)
5        n = len(classroom[0])
6        litter = []
7        start = None
8        for i in range(m):
9            for j in range(n):
10                if classroom[i][j] == 'S':
11                    start = (i, j)
12                elif classroom[i][j] == 'L':
13                    litter.append((i, j))
14        litter_index = {}
15        for i in range(len(litter)):
16            litter_index[litter[i]] = i
17        all_collected = (1 << len(litter)) - 1
18        queue = deque()
19        queue.append((start[0], start[1], 0, energy, 0))
20        visited = set()
21        visited.add((start[0], start[1], 0, energy))
22        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
23        while queue:
24            r, c, mask, remaining, moves = queue.popleft()
25            if mask == all_collected:
26                return moves
27            for dr, dc in directions:
28                nr = r + dr
29                nc = c + dc
30                if nr < 0 or nr >= m or nc < 0 or nc >= n:
31                    continue
32                if classroom[nr][nc] == 'X':
33                    continue
34                if remaining == 0:
35                    continue
36                new_energy = remaining - 1
37                new_mask = mask
38                if classroom[nr][nc] == 'L':
39                    bit = litter_index[(nr, nc)]
40                    new_mask |= (1 << bit)
41                if classroom[nr][nc] == 'R':
42                    new_energy = energy
43                state = (nr, nc, new_mask, new_energy)
44                if state not in visited:
45                    visited.add(state)
46                    queue.append((nr, nc, new_mask, new_energy, moves + 1))
47        return -1
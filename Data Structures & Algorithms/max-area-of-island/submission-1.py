class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0

        N, M = len(grid), len(grid[0])
        
        discovered = set()

        directions = [
            (1,0),
            (-1,0),
            (0,-1),
            (0, 1)
        ]

        max_area = 0
        def bfs(i, j):
            if (i, j) in discovered:
                return 0
            
            if grid[i][j] != 1:
                return 0
            
            curr_area = 0

            queue = deque()
            queue.append((i,j))

            while queue:
                r, c = queue.popleft()
                if (r,c) in discovered:
                    continue
                curr_area += 1

                discovered.add((r,c))
                for right, left in directions:
                    if (r+right, c + left) in discovered:
                        continue

                    if 0 <= r + right < N and 0 <= c + left < M:
                        if grid[r+right][c+left] == 1:
                            queue.append((r+right, c + left))
            
            return curr_area
        
        for i in range(N):
            for j in range(M):
                if grid[i][j] == 1 and (i,j) not in discovered:
                    print("call")
                    max_area = max(max_area, bfs(i,j))

        return max_area


            

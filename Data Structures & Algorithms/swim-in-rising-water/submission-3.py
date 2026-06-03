class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0

        pq = []
        N = len(grid)

        heapq.heappush(pq, (grid[0][0], 0, 0))

        visited = set()
        while pq:

            t, r, c = heapq.heappop(pq)

            if (r, c) in visited:
                continue
                
            visited.add((r,c))
            if (r, c) == (N-1, N-1):
                return t

            if r > 0 and (r - 1, c) not in visited:
                heapq.heappush(pq, (max(t, grid[r-1][c]), r-1, c))
            if c > 0 and (r, c-1) not in visited:
                heapq.heappush(pq, (max(t, grid[r][c-1]), r, c-1))
            if r < N-1 and (r + 1, c) not in visited:
                heapq.heappush(pq, (max(t, grid[r+1][c]), r+1, c))
            if c < N-1 and (r, c + 1) not in visited:
                heapq.heappush(pq, (max(t, grid[r][c+1]), r, c+1))
        
            
            
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        
        pq = stones
        heapq.heapify_max(pq)

        while len(pq) > 1:
            top = heapq.heappop_max(pq)
            sec = heapq.heappop_max(pq)

            if top != sec:
                heapq.heappush_max(pq, (top - sec))
        
        return pq[0] if pq else 0


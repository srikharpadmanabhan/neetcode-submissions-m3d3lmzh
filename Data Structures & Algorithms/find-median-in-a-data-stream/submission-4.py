class MedianFinder:

    def __init__(self):
        self.max_heap = []
        self.min_heap = []
        self.length = 0

    def addNum(self, num: int) -> None:
        if not self.max_heap or num <= self.max_heap[0]:
            heapq.heappush_max(self.max_heap, num)
        else:
            heapq.heappush(self.min_heap, num)
        
        if len(self.max_heap) - len(self.min_heap) >= 2:
            top = heapq.heappop_max(self.max_heap)
            heapq.heappush(self.min_heap, top)
        elif len(self.min_heap) - len(self.max_heap) >= 2:
            top = heapq.heappop(self.min_heap)
            heapq.heappush_max(self.max_heap, top)

    def findMedian(self) -> float:
        print(self.max_heap, self.min_heap)
        if len(self.max_heap) > len(self.min_heap):
            return self.max_heap[0]
        elif len(self.min_heap) > len(self.max_heap):
            return self.min_heap[0]
        else:
            return (self.min_heap[0] + self.max_heap[0]) / 2
        
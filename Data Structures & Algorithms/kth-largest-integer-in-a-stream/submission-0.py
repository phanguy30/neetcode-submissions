import heapq

class KthLargest:
    def __init__(self, k: int, nums: list[int]):
        self.k = k
        self.heap = nums
        heapq.heapify(self.heap) # Transform list into a heap in-place
        
        # Keep only the k largest elements
        while len(self.heap) > k:
            heapq.heappop(self.heap)

    def add(self, val: int) -> int:
        # Add the new value
        heapq.heappush(self.heap, val)
        
        # If we exceed size k, remove the smallest element
        if len(self.heap) > self.k:
            heapq.heappop(self.heap)
            
        # The root of a min-heap of size k is the kth largest element overall
        return self.heap[0]
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res = {}
        for num in nums:
            res[num]= 1+ res.get(num,0)
        heap = []
        for num in res.keys():
            heapq.heappush(heap, (res[num], num))
            
            if len(heap)>k:
                heapq.heappop(heap)
            
        res = []
        for i in range(k):
            res.append(heapq.heappop(heap)[1])
        return res

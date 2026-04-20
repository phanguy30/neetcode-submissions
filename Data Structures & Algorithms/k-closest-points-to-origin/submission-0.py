from math import sqrt
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        distances  = []
        for point in points:
            x,y = point[0], point[1]
            distances.append((-(x**2 + y**2), [x,y]))
        heapq.heapify(distances)
        while len(distances) > k:
            heapq.heappop(distances)
        return [point for (dist, point) in distances]



        
    
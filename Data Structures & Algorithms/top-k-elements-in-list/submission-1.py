class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res = {}
        for num in nums:
            res[num]= 1+ res.get(num,0)
        res_list = []
        for key,value in res.items():
            res_list.append((value,key))
        res_list.sort(reverse = True)
        out = []
        for i in range(k):
            out.append(res_list[i][1])
        return out
            
        
        
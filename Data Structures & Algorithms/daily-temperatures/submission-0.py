class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        my_stack = []
        res = [0]*len(temperatures)
        for i,v in enumerate(temperatures):
        
            while my_stack and my_stack[len(my_stack)-1][1] < v:
                temp = my_stack.pop()
                res[temp[0]] = i - temp[0]


        
            my_stack.append((i,v))
        return res

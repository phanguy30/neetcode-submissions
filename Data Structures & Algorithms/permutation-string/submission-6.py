class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2): return False
        my_dict1 = {}
        my_dict2 = {}
       
        
            
        for l in range(len(s1)):
            my_dict1[s1[l]] = my_dict1.get(s1[l],0)+1
            my_dict2[s2[l]] = my_dict2.get(s2[l],0)+1

        l = 0
        r = len(s1)
        while r < len(s2):
            if my_dict1 == my_dict2:
                return True
            else:
                
                my_dict2[s2[r]]= my_dict2.get(s2[r],0)+1
                my_dict2[s2[l]]-=1
                if my_dict2[s2[l]] == 0:
                    del my_dict2[s2[l]]
                r+=1 
                l+=1
        return my_dict1 == my_dict2


            
        
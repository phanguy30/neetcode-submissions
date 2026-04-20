class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res =[]
        for i,v in enumerate(nums):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            if nums[i] > 0:
                continue
            
            l = i+1
            r = len(nums)-1
            

            while r > l:
                curr_sum = nums[i] + nums[l]+ nums[r]
                if curr_sum > 0:
                    r-=1
                elif curr_sum <0:
                    l+=1
                else:
                    res.append([nums[i], nums[l],nums[r]])
                    r-=1
                    l+=1
                    while l< len(nums) and nums[l-1] == nums[l]:
                        l+=1
                    while r>0 and nums[r+1] == nums[r]:
                        r-=1
        return res
                        




        
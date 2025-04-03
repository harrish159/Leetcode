class Solution(object):
    def triangleType(self, nums):
        res=set(nums)
        count=0
        if len(res)==1:
            return 'equilateral'
        elif len(res)==2:
            for i in range(0,len(nums)):
                tot=sum(nums)-nums[i]
                if(tot>nums[i]):
                    count+=1
                if count==3:
                    return 'isosceles'
        elif len(res)==3:
            for i in range(0,len(nums)):
                tot=sum(nums)-nums[i]
                if(tot>nums[i]):
                    count+=1
                if count==3:
                    return 'scalene'
        return 'none'
        
        
        
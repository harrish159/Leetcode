class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        l,r=0,0
        count=0
        maxi=0
        for i in range(0,len(nums)):
            if(nums[r]==1):
                r+=1
                count+=1
                if(count>maxi):
                    maxi=count
            else:
                count=0
                r+=1
                l+=r+1
        return maxi
            
            
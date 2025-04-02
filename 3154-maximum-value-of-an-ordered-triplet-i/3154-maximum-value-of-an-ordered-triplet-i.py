class Solution(object):
    def maximumTripletValue(self, nums):
        maxi = 0
        
        for i in range(len(nums)):
            count = 0
            for j in range(i + 1, len(nums)):  
                count = max(count, nums[i] - nums[j])
                for k in range(j + 1, len(nums)): 
                    maxi = max(maxi, count * nums[k])
        
        return maxi

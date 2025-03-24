class Solution(object):
    def findLengthOfLCIS(self, nums):
        if not nums:
            return 0

        l = 0  
        max_length = 1 

        for r in range(1, len(nums)):
            if nums[r] > nums[r - 1]:  
                max_length = max(max_length, r - l + 1)
            else:
                l = r 
        return max_length
        
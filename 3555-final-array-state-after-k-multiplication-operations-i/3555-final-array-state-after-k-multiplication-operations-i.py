class Solution(object):
    def getFinalState(self, nums, k, multiplier):
        for i in range(k):
            min_ind=nums.index(min(nums))
            num=nums[min_ind]*multiplier
            nums[min_ind]=num
        return(nums)
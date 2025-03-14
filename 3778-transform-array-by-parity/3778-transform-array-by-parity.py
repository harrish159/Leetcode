class Solution(object):
    def transformArray(self, nums):
        for i in range(0,len(nums)):
            if nums[i]%2==0:
                nums[i]=0
            else:
                nums[i]=1
        return sorted(nums)
        
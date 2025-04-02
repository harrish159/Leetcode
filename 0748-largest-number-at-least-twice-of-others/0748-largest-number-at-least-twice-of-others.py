class Solution(object):
    def dominantIndex(self, nums):
        s=max(nums)
        index=nums.index(s)
        nums.sort(reverse=True)
        if nums[0] >= nums[1] * 2:
            return index
        return -1

        
        
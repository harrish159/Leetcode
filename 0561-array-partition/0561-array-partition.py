class Solution(object):
    def arrayPairSum(self, nums):
        mini=0
        nums.sort()
        for i in range(0,len(nums),2):
                for j in range(i+1,len(nums)):
                    mini=mini+min(nums[i],nums[j])
                    break
        return mini
class Solution(object):
    def createTargetArray(self, nums, index):
        res=[]
        for i in range(0,len(nums)):
            ind = index[i]
            num = nums[i]
            res.insert(ind,num)
        return res
class Solution(object):
    def shuffle(self, nums, n):
        start=0
        end=n
        res=[]
        while(end<len(nums)):
            res.append(nums[start])
            res.append(nums[end])
            start+=1
            end+=1
        return res
class Solution(object):
    def numberGame(self, nums):
        nums.sort()
        res=[]
        while(nums):
            num1=nums.pop(0)
            num2=nums.pop(0)
            res.append(num2)
            res.append(num1)
        return res
        
class Solution(object):
    def countDistinctIntegers(self, nums):
        nums1=[]
        for i in range(0,len(nums)):
            num1 = nums1.append(int(str(nums[i])[::-1]))
        nums.extend(nums1)
        res=set(nums)
        return len(res)
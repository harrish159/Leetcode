class Solution(object):
    def maxProductDifference(self, nums):
         nums.sort()
         return abs((nums[0]*nums[1])-(nums[len(nums)-1]*nums[len(nums)-2]))
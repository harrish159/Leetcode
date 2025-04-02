class Solution(object):
    def minPairSum(self, nums):
        nums.sort()
        maxi=0
        l=0
        r=len(nums)-1
        while(l<=r):
            maxi = max(maxi,nums[l]+nums[r])
            l+=1
            r-=1
        return maxi
        
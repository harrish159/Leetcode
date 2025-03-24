class Solution(object):
    def minimumAverage(self, nums):
        nums.sort()
        avg=[]
        while(nums):
            mini=(nums.pop(0))
            maxi=(nums.pop(-1))
            avg.append((mini+maxi)/2.0)
        return min(avg)
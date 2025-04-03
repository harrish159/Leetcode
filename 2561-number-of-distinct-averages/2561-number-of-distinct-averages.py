class Solution(object):
    def distinctAverages(self, nums):
        res = set() 
        nums.sort()
        i, j = 0, len(nums) - 1
        while i < j:
            avg = (nums[i] + nums[j]) / 2.0
            res.add(avg)
            i += 1
            j -= 1

        return len(res) 
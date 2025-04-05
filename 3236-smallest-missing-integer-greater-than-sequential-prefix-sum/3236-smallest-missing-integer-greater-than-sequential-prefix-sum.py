class Solution(object):
    def missingInteger(self, nums):
        seq = set()
        seq.add(nums[0]) 
        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1] + 1:
                seq.add(nums[i])
            else:
                break  

        total = sum(seq)
        while True:
            if total not in nums:
                return total
            total += 1

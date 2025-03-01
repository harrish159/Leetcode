class Solution(object):
    def applyOperations(self, nums):
        n = len(nums)
    
    # Step 1: Apply the operations sequentially
        for i in range(n - 1):
            if nums[i] == nums[i + 1] and nums[i] != 0:
                nums[i] *= 2
                nums[i + 1] = 0
    
    # Step 2: Shift non-zero elements to the front
        result = [num for num in nums if num != 0]
    
    # Step 3: Fill the remaining positions with zeros
        result.extend([0] * (n - len(result)))
    
        return result
        
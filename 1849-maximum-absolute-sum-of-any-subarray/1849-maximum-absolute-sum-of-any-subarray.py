class Solution(object):
    def maxAbsoluteSum(self, nums):
        max_sum = min_sum = 0
        curr_max = curr_min = 0

        for num in nums:
            curr_max = max(curr_max + num, num)  # Standard Kadane’s for max subarray sum
            curr_min = min(curr_min + num, num)  # Reverse Kadane’s for min subarray sum
            max_sum = max(max_sum, curr_max)
            min_sum = min(min_sum, curr_min)

        return max(max_sum, abs(min_sum))
        
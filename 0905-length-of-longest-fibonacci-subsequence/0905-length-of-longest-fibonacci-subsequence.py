class Solution(object):
    def lenLongestFibSubseq(self,arr):
        index = {x: i for i, x in enumerate(arr)}
        n = len(arr)
        dp = {}
        max_len = 0

        for i in range(n):
            for j in range(i):
                x = arr[i] - arr[j]  # We need arr[k] such that arr[k] + arr[j] = arr[i]
                if x in index and index[x] < j:
                    k = index[x]
                    dp[j, i] = dp.get((k, j), 2) + 1
                    max_len = max(max_len, dp[j, i])
    
        return max_len if max_len > 2 else 0

        
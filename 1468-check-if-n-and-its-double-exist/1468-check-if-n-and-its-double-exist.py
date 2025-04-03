class Solution(object):
    def checkIfExist(self, arr):
        for i in range(0,len(arr)):
            for j in range(0,len(arr)):
                if arr[i]==arr[j]*2 and i!=j:
                    return True
        return False    
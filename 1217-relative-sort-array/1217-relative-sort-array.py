class Solution(object):
    def relativeSortArray(self, arr1, arr2):
        arr1.sort()
        res=[]
        for i in range(0,len(arr2)):
            count1=arr1.count(arr2[i])
            while(count1>0):
                res.append(arr2[i])
                count1-=1
        for i in arr1:
            if i not in arr2:
                res.append(i)
        return res
        
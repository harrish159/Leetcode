class Solution(object):
    def kthDistinct(self, arr, k):
        list1=[]
        for i in arr:
            if arr.count(i)==1:
                list1.append(i)
        if k>len(list1):
            return ""
        return list1[k-1]
            
        
class Solution(object):
    def pivotArray(self, nums, pivot):
        list1=[]
        list2=[]
        list3=[]
        for i in nums:
            if i<pivot:
                list1.append(i)
            elif i>pivot:
                list3.append(i)
            else:
                list2.append(i)
        return list1+list2+list3
class Solution(object):
    def findMissingAndRepeatedValues(self, grid):
        list1=[]
        for i in grid:
            for j in i:
                list1.append(j)
        miss=0
        rep=0
        for i in list1:
            if list1.count(i)>1:
                rep=i
        for i in range(1,len(list1)+1):
            if i not in list1:
                miss=i
                break
        return [rep,miss]
        
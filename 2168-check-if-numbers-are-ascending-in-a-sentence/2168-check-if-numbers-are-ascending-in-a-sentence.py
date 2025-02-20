class Solution(object):
    def areNumbersAscending(self, s):
        list1=s.split()
        num=[int(x) for x in list1 if x.isdigit()]
        temp=num[0]
        flag=0
        for i in range(1,len(num)):
            if temp>=num[i]:
                flag=1
                break
            temp=num[i]
        if flag==0:
            return True
        return False
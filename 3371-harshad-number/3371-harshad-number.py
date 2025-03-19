class Solution(object):
    def sumOfTheDigitsOfHarshadNumber(self, x):
        x=str(x)
        tot=0
        for i in x:
            tot+=int(i)
        if int(x)%tot==0:
            return tot
        return -1
        
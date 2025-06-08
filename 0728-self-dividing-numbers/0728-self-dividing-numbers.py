class Solution(object):

    def check(self,num):
        ini=num
        while num>0:
            dig=num%10
            if  dig==0 or ini%dig!=0 :
                return False
            num/=10
        return True 

    def selfDividingNumbers(self, left, right):
        res=[]
        for i in range(left,right+1):
            if self.check(i):
                res.append(i)
        return res

        
        
class Solution(object):
    def trailingZeroes(self, n):
        num=1
        for i in range(n,0,-1):
            num=num*i
        num=str(num)[::-1]
        count=0
        for i in num:
            if i=='0':
                count+=1
            else:
                break
        return count
        

        
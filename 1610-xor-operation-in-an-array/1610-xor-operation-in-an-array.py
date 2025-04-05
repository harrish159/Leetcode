class Solution(object):
    def xorOperation(self, n, start):
        s=[]
        for i in range(n):
            num=start+2 * i
            s.append(num)
        res=s[0]
        for i in range(1,len(s)):
            res=res ^ s[i]
        return res
        
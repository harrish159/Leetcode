class Solution(object):
    def replaceDigits(self, s):
        ch=0
        result=''
        for i in range(0,len(s)):
            if i%2==0:
                ch=s[i]
                result+=ch
            else:
                num=int(s[i])
                char=chr(ord(ch)+num)
                result+=char
        return result
        
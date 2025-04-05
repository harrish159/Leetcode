class Solution(object):
    def judgeCircle(self, moves):
        num=0
        num1=0
        for i in moves:
            if i=='U':
                num+=1

            elif i=='D':
                num-=1

            elif i=='L':
                num1-=1

            elif i=='R':
                num1+=1
        if num==0 and num1==0:
            return True
        return False

        
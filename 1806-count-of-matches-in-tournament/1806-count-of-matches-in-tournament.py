class Solution(object):
    def numberOfMatches(self, n):
        mat,adv=0,0
        while n>=2:
            if (n%2==0):
                mat=mat+(n/2)
                adv=(n/2)
                n=adv
            else:
                mat+=(n-1)/2
                adv=((n-1)/2)+1
                n=adv

        return mat
                

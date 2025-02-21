class Solution(object):
    def alternateDigitSum(self, n):
        n=str(n)
        even=[int(n[i]) for i in range(0,len(n)) if i%2==0]
        odd=[int(n[i]) for i in range(0,len(n)) if i%2!=0]
        return sum(even)-sum(odd)
        
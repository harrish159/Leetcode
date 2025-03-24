class Solution(object):
    def maxPower(self, s):
        l,r=0,0
        count=0
        maxi=0
        while(r<len(s)):
            if (s[l]==s[r]):
                r+=1
            else:
                l=r
            count=r-l
            maxi = max(maxi, count)
        return maxi
        
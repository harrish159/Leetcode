class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        maxi=max(candies)
        res=[]
        
        for i in range(0,len(candies)):
            if candies[i]+extraCandies >= maxi : 
                res.append(True)
            else:
                res.append(False)
        return res
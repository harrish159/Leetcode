class Solution(object):
    def maximumWealth(self, accounts):
        maxi=0
        for i in accounts:
            if sum(i)>maxi:
                maxi=sum(i)
        return maxi


        
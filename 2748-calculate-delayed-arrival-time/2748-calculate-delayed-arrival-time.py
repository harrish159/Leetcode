class Solution(object):
    def findDelayedArrivalTime(self, a,d):
        tot=a+d
        if(tot>=24):
            return(tot%24)
        return tot
        
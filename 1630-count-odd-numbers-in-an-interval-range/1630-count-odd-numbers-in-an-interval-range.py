class Solution(object):
    def countOdds(self, low, high):
        count=0
        if (high-low+1)%2==0:
            count=(high-low+1)/2
        else:
            count=(high-low+1)/2
            if high%2!=0:
                count+=1
        return count
        
class Solution(object):
    def isBalanced(self, num):
        odd=[int(num[i]) for i in range(0,len(num)) if i%2!=0]
        even=[int(num[i]) for i in range(0,len(num)) if i%2==0]
        return sum(odd)==sum(even)
        
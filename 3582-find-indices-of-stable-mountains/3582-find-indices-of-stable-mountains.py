class Solution(object):
    def stableMountains(self, height, threshold):
        index=[]
        for i in range(1,len(height)):
            if height[i-1]>threshold:
                index.append(i)
        return index
        
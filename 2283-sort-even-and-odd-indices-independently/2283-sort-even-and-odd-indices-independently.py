class Solution(object):
    def sortEvenOdd(self, nums):
        even=[]
        odd=[]
        res=[]
        for i in range(0,len(nums)):
            if i%2==0:
                even.append(nums[i])
            else:
                odd.append(nums[i])
        even.sort()
        odd.sort(reverse=True)
        j,z=0,0
        for i in range(0,len(nums)):
            if i%2==0:
                res.append(even[j])
                j+=1
            else:
                res.append(odd[z])
                z+=1
        return res
class Solution(object):
    def minDeletionSize(self, strs):
        transposed = list(map(''.join, zip(*strs)))
        count=0
        for word in transposed:
            for i in range(1,len(word)):
                if word[i]<word[i-1]:
                    flag=0
                    count+=1
                    print(word)
                    break
        return count



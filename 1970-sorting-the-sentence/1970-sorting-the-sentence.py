class Solution(object):
    def sortSentence(self, s):
        s=s.split()
        list1 = [None] * len(s)
        for word in s:
            length=len(word)
            num=int(word[-1])
            ch=word[:length-1]
            list1[num-1]=ch
        return ' '.join(list1)
            
        
class Solution(object):
    def reverseWords(self, s):
        list1=s.split()
        list2=[]
        for i in list1:
            list2.append(i[::-1])
        return ' '.join(list2)
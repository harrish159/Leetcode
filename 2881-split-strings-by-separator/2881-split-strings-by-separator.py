class Solution(object):
    def splitWordsBySeparator(self, words, separator):
        result=[]
        for word in words:
            list1=word.split(separator)
            result.extend(list1)
        return filter(None,result)
class Solution(object):
    def countSeniors(self, details):
        count=0
        for i in details:
            age=i[11:13]
            if age>'60':
                count+=1 
        return count
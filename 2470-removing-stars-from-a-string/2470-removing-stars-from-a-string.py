class Solution(object):
    def removeStars(self, s):
        
        res = []
        for ch in s:
            if ch == '*':
                if res:
                    res.pop()
            else:
                res.append(ch)
        return ''.join(res)

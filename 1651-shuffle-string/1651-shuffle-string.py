class Solution(object):
    def restoreString(self, s, indices):
        res = [None] * len(s)
        for i in indices:
            res[indices[i]]=s[i]
        return ''.join(res)
        